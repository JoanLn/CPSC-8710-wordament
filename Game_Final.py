import tkinter as tk
import random
from itertools import product
import nltk
from nltk.corpus import words

nltk.download('words')
quit_flag = False

class WordamentGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordament Game")
        self.english_words = set(words.words())
        self.grid = self.generate_grid()
        self.current_word = []
        self.found_words = set()
        self.all_valid_words = self.get_all_valid_words()
        
        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        
        for i in range(4):
            for j in range(4):
                btn = tk.Button(self.root, text=self.grid[i][j], width=5, height=2, 
                                command=lambda i=i, j=j: self.button_click(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn
                
        self.word_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.word_label.grid(row=4, column=0, columnspan=4)
        
        self.message_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.message_label.grid(row=6, column=0, columnspan=4)
        
        self.remaining_label = tk.Label(self.root, text=f"Words Remaining: {len(self.all_valid_words)}", font=("Arial", 12))
        self.remaining_label.grid(row=7, column=0, columnspan=4)
        
        self.submit_btn = tk.Button(self.root, text="Submit", command=self.submit_word)
        self.submit_btn.grid(row=5, column=0, columnspan=4)
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

    def button_click(self, i, j):
        if (i, j) not in self.current_word:
            self.current_word.append((i, j))
            self.word_label["text"] += self.grid[i][j]
            self.buttons[i][j].config(state=tk.DISABLED)
    
    def submit_word(self):
        word = self.word_label["text"]
        if word in self.all_valid_words:
            if word not in self.found_words:
                self.found_words.add(word)
                remaining_words = len(self.all_valid_words) - len(self.found_words)
                self.remaining_label["text"] = f"Words Remaining: {remaining_words}"
                self.message_label["text"] = f"{word} is a valid word!"
                if len(self.found_words) == 3:
                    self.message_label["text"] = "Congratulations! You won!"
                    self.root.after(1000, self.end_game)   
            else:
                self.message_label["text"] = f"You've already found the word {word}."
        else:
            self.message_label["text"] = f"{word} is not a valid word."
        
        self.reset_game()

    def end_game(self):
        if not self.quit:  
            self.quit_flag = True 
            self.root.destroy()
            game2_root = tk.Tk()  
            game2 = PasswordGame(game2_root, list(self.found_words)) 
            game2_root.mainloop()

    def reset_game(self):
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].config(state=tk.NORMAL)
        
        self.word_label["text"] = ""
        self.current_word = []

    def get_20_words(self):
        return list(self.all_valid_words)[:20]
    
    def run(self): 
        self.root.mainloop()
        return list(self.found_words)
    
    def restart_game(self):
        self.root.destroy()
        main_sequence()

    def quit_game(self):
        self.quit = True
        self.root.destroy()

def display_end_options(self):
    restart_btn = tk.Button(self.root, text="Restart", command=self.restart_game)
    restart_btn.grid(row=8, column=0, columnspan=2)

    quit_btn = tk.Button(self.root, text="Quit", command=self.quit_game)
    quit_btn.grid(row=8, column=2, columnspan=2)


def run_wordament_game():
    global quit_flag
    root = tk.Tk()
    game = WordamentGame(root)
    root.mainloop()
    return game.get_20_words() if not quit_flag else []


class PasswordGame:
    def __init__(self, root, words):
        self.root = root
        self.root.title("Password Game")

        self.words = words
        self.word_to_guess = random.choice(self.words)
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 3 

        self.word_display = ["_" if letter.isalpha() else letter for letter in self.word_to_guess]
        self.word_label = tk.Label(self.root, text=" ".join(self.word_display), font=("Arial", 20))
        self.word_label.grid(row=0, column=0, columnspan=26)

        self.hangman_label = tk.Label(self.root, text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}", font=("Arial", 16))
        self.hangman_label.grid(row=1, column=0, columnspan=26)

        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.root, text=letter, width=2, height=1, 
                            command=lambda letter=letter: self.letter_click(letter))
            btn.grid(row=2 + i//13, column=i%13)

    def letter_click(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.add(letter)
            
            if letter in self.word_to_guess:
                for idx, char in enumerate(self.word_to_guess):
                    if char == letter:
                        self.word_display[idx] = letter
            else:
                self.wrong_guesses += 1
            
            self.word_label.config(text=" ".join(self.word_display))
            self.hangman_label.config(text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")

            if self.wrong_guesses >= self.max_wrong_guesses:
                self.end_game(lose=True)
            elif "_" not in self.word_display:
                self.end_game(lose=False)

    def end_game(self, lose):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        if lose:
            message = f"You lost! The word was {self.word_to_guess}."
        else:
            message = "Congratulations! You won!"
        
        self.word_label = tk.Label(self.root, text=message, font=("Arial", 20))
        self.word_label.grid(row=0, column=0, columnspan=26)
    
        restart_btn = tk.Button(self.root, text="Restart Entire Game", command=self.restart_game)
        restart_btn.grid(row=2, column=0, columnspan=13)

        quit_btn = tk.Button(self.root, text="Quit", command=self.quit_game)
        quit_btn.grid(row=2, column=13, columnspan=13)

    def restart_game(self):
        self.root.destroy()
        main_sequence()

    def quit_game(self):
        global quit_flag
        quit_flag = True
        self.root.destroy()

def run_password_game(words):
    if words: 
        root = tk.Tk()
        game = PasswordGame(root, words)
        root.mainloop()

def main_sequence():
    global quit_flag
    quit_flag = False
    words_to_use = run_wordament_game()
    if not quit_flag:
        run_password_game(words_to_use)

if __name__ == "__main__":
    main_sequence()
    