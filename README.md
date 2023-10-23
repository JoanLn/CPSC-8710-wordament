

![logo-png](https://github.com/JoanLn/CPSC-8710-wordament/assets/65409705/752c1ee5-ec38-477a-b090-f38b76887c58)



# Lexilock

Welcome to LexiLock, the ultimate word puzzle game designed to challenge and expand your vocabulary. First up, In Wordament, your goal is to find as many words as possible by connecting letters. Whether you're a casual gamer or a word enthusiast, Wordament offers an engaging and educational experience. Next, Password Game which is an excellent exercise in logic and deduction, challenging players to analyze feedback and make educated guesses to decipher the hidden password.
Delve into the letter grid, refine your linguistic abilities, and embark on your Wordament adventure today!

## Objective

 Embark on a journey through the world of letters and vocabulary in the Wordament Challenge. Your task is to collect words from a grid of letters. Once you've mastered the Wordament Challenge, you'll utilize the words you've collected as clues in the Password Generator Puzzles. Utilize your adept command of language and your knack for deciphering codes to emerge victorious in this captivating dual endeavor crafting a one-of-a-kind word puzzle odyssey.
## Game Developers
This endeavor has been embraced by a team of passionate developers, bound together by their shared enthusiasm for creating an enthralling word puzzle game. Allow us to introduce the talented individuals who have turned this concept into a tangible reality:

- [@Joanna Lin](https://github.com/JoanLn)
- [@Sushanth Reddy Racham Reddy](https://github.com/sushanth-0)
- [@Venkata Sai Ganesh Varun Duggirala](https://github.com/DVSG09)



## Setup and Installation ⚙

Step 1 
Clone the repository
https://github.com/JoanLn/CPSC-8710-wordament.git

Step 2
To initiate your journey into the world of word puzzles, ensure the installation of the mentioned dependencies.

- Python 3
- Flask
- NLTK
- HTML/CSS

Step 3: 

 Run the file using "flask run"

 Step 4:

Open web browser then run http://127.0.0.1:5000 to enjoy the seamless experience of world of words!

Alternate way to enjoy the game : https://wordament.fly.dev/
## Technology Used 💾

- Python -> 
- Flask -> Flask serves as the web framework for managing routing and handling requests.
- HTML/CSS -> HTML and CSS have been employed to craft an user-friendly interface on the frontend.





## Third-Party Assets and Code
Pumpkin: Halloween Jack O Lantern png download - 512*512 - Free Transparent Pumpkin png Download. - CleanPNG / KissPNG
Background: Free AI Image | Halloween background with scary pumpkins candles and bats in a dark forest at night (freepik.com)
## Reflection on the Design and Development Process
The first challenge is to find a way to build a web application with python code. Since we don’t have any related experience before, it’s hard to begin. After reading some documentation, we decided to use Flask, which is a micro web framework written in Python. After building the page with HTML and CSS, the python application can run with the web page. There’s the second challenge, how to make a dynamic web page without refreshing the page. Since we need to prevent the player from choosing the same letter in a guessing turn, we decide to disable the letter button in the word grid after the letter being chosen. However, because we call the function with a submit type button and the register route, the page will refresh every time the player clicks any button on the webpage. To solve the problem, we add a short javascript in the HTML file to listen to the button and run the function without reloading the page. The last challenge is to deploy the web application. We had tried the AWS Elastic Beanstalk service, Netlify and Fly.io, and none of them worked at first. We decided to use the fly.io at the end since it's the most common I heard. After reading the documents and the discussion on the forum of fly.io, trying different settings worked at the end. 
There’s still a function that we are not successfully implementing, which is to force the player to only connect the adjustment letter when guessing the word.

