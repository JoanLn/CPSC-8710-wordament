import tkinter as tk
import random
from itertools import product
import nltk
from nltk.corpus import words

from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)

keybord = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "", ""]
#
# part1 - wordament 
#
class WordamentGame:
    def __init__(self):#, root):

        self.english_words = set(words.words())
        self.grid = self.generate_grid()
        self.current_word = []
        self.found_words = set()
        self.all_valid_words = self.get_all_valid_words()
                    
        self.word_label = ""
        
        self.message_label = ""
        
        self.remaining_label = f"Words Remaining: {len(self.all_valid_words)}" 
        self.quit = False

    def generate_grid(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            grid = [[random.choice(letters) for _ in range(4)] for _ in range(4)]
            valid_words = self.get_all_valid_words(grid)
            if len(valid_words) >= 50:  # Checking for grids with at least 50 valid words
                return grid


    def get_all_valid_words(self, grid=None):
        if grid is None:
            grid = self.grid
        directions = list(product([-1, 0, 1], repeat=2))
        directions.remove((0, 0))
        
        def is_valid(i, j):
            return 0 <= i < 4 and 0 <= j < 4
        
        def dfs(i, j, current_word, visited):
            if len(current_word) == 4:
                if current_word.lower() in self.english_words:
                    words_found.add(current_word)
                return
            
            for x, y in directions:
                ni, nj = i + x, j + y
                if is_valid(ni, nj) and (ni, nj) not in visited:
                    dfs(ni, nj, current_word + grid[ni][nj], visited | {(ni, nj)})
        
        words_found = set()
        for i in range(4):
            for j in range(4):
                dfs(i, j, grid[i][j], {(i, j)})
        
        return words_found

#
# part2 - wordament 
#

class PasswordGame:
    def __init__(self, words):

        self.words = words
        self.word_to_guess = random.choice(list(self.words))
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 3 

        self.word_display = ["_" if letter.isalpha() else letter for letter in self.word_to_guess]
        self.word_label = " ".join(self.word_display)

        self.hangman_label = f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}"

    def end_game(self, lose):
            
        if lose:
            message = f"You lost! The word was {self.word_to_guess}."
        else:
            message = "Congratulations! You won!"
        
    def restart_game(self):
        main_sequence()

    def quit_game(self):
        global quit_flag
        quit_flag = True


global game
game = WordamentGame()
game2 = PasswordGame(['init'])

@app.route("/enter", methods=['POST'])
def button_click():
    word_id = request.form["word_id"]
    game.current_word.append(word_id)
    game.word_label += word_id
    flash(game.word_label, "word")
    return render_template("index.html", remaining_words = game.remaining_label, grid = game.grid)

@app.route("/guess", methods=["POST"])
def submit_word():
    word = game.word_label
    print(f"word: {word}")
    if word in game.all_valid_words:
        if word not in game.found_words:
            game.found_words.add(word)
            remaining_words = len(game.all_valid_words) - len(game.found_words)
            game.remaining_label= f"Words Remaining: {remaining_words}"
            game.message_label = f"{word} is a valid word!"
            flash(f"{word} is a valid word!", "message")
            if len(game.found_words) == 3:
                game.message_label = "Congratulations! You won!"
                flash("Congratulations! You won!", "message")
                game2 = PasswordGame(game.found_words)
                print("guess:" + game2.word_to_guess)
                print("return render_template")

                reset_game1(game)
                #game = reset_game1(game)    
                print(game.all_valid_words)           
                return render_template("password.html", keybord = keybord, word_to_guess =  game2.word_to_guess)
        else:
            game.message_label = f"You've already found the word {word}."
            flash(f"You've already found the word {word}.", "message")
            
    else:
        game.message_label = f"{word} is not a valid word."
        flash(f"{word} is not a valid word.", "message")
        
    reset_guess()

    return render_template("index.html", remaining_words = game.remaining_label, grid = game.grid)

def end_game():
    if not game.quit:  
        game.quit_flag = True 

def reset_guess():       
    game.word_label = ""
    game.current_word = []

def reset_game1(game):       
    #global game
    game.word_label = ""
    game.current_word = []
    game.found_words = set()
    game = WordamentGame()
    return game


def reset_game2(game2):   
    game2.wrong_guesses = 0
    game2.guessed_letters = set()  
    game2.word_display = ["_" if letter.isalpha() else letter for letter in game2.word_to_guess]
    game2 = PasswordGame(['init'])  

def get_20_words():
    return list(game.all_valid_words)[:20]
    

@app.route("/restart", methods=['POST'])    
def restart_game():
    #game = WordamentGame()
    print("Restart Game")
    #reset_game1(game)
    #reset_game2(game2)

    print(game.all_valid_words)
    print(game.word_label)
    print(game.grid)
    return render_template("index.html", remaining_words = game.remaining_label, grid = game.grid)

def quit_game():
    game.quit = True

@app.route("/key", methods=["POST"])
def letter_click():    
    letter = request.form["key_id"]
    print(f"guess: {letter}")
    word_to_guess = request.form["guess_word"]
    print(f"Word to guess: {word_to_guess}")
    
    if letter not in game2.guessed_letters:
        print("Letter never guess")
        game2.guessed_letters.add(letter)
            
        if letter in word_to_guess:
            print("Letter in word")
            for idx, char in enumerate(word_to_guess):
                if char == letter:
                    game2.word_display[idx] = letter
        else:
            print("wrong guess")
            game2.wrong_guesses += 1
            
        game2.word_label = " ".join(game2.word_display)
        game2.hangman_label = f"Wrong guesses: {game2.wrong_guesses}/{game2.max_wrong_guesses}"

        flash(f" ".join(game2.word_display) , "word_label")
        flash(f"Wrong guesses: {game2.wrong_guesses}/{game2.max_wrong_guesses}", "hangman_label")

        if game2.wrong_guesses >= game2.max_wrong_guesses:
            reset_game2(game2)
            return render_template("lose.html", word = word_to_guess)
        elif "_" not in game2.word_display:
            reset_game2(game2)
            return render_template("win.html", word = word_to_guess)
    
    return render_template("password.html", keybord = keybord, word_to_guess = word_to_guess)

@app.route('/')
def hello(name=None):
    app.secret_key = 'keep it secret'
    print(game.all_valid_words)
    print(game.grid)
    return render_template("index.html", remaining_words = game.remaining_label, grid = game.grid)