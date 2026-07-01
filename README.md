# 🐍 CodeAlpha Python Programming Internship Projects

## 📌 Overview

This repository contains the Python projects completed during my **Python Programming Internship** at **CodeAlpha**. These projects helped me strengthen my understanding of Python fundamentals through hands-on implementation of real-world programming concepts.


# Task1:- Hangman Game

A simple **console-based Hangman Game** built using **Python**. In this game, the player tries to guess a randomly selected word one letter at a time. The player has **6 incorrect attempts** to guess the word before the game ends.

This project was developed as **Task 1** of the **CodeAlpha Python Programming Internship**.

---

## 📌 Features

- 🎲 Random word selection from a predefined list
- 🔤 Letter-by-letter guessing
- ❌ Maximum of 6 incorrect guesses
- 🔁 Prevents duplicate guesses
- 🏆 Win/Lose game messages
- 💻 Simple and interactive command-line interface

---

## 🛠️ Technologies Used

- Python 3.x

### Concepts Used
- `random` Module
- Lists
- Strings
- While Loop
- If-Else Statements
- User Input & Output

---

## 📂 Project Structure

```
Hangman-Game/
│── hangman.py
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/tejasjangid42-rgb/Hangman-Game.git
```

2. Navigate to the project folder:

```bash
cd Hangman-Game
```

3. Run the program:

```bash
python hangman.py
```

---

## 🎮 Sample Output

```text
🎮 Welcome to Hangman!

Word: _ _ _ _ _ _

Incorrect guesses left: 6

Enter a letter: p

✅ Correct guess!

Word: p _ _ _ _ _
```

---

## 📖 How to Play

1. Run the Python program.
2. A random word is selected from the predefined list.
3. Enter one letter at a time.
4. If the guessed letter is correct, it is revealed in the word.
5. If the guess is incorrect, one attempt is deducted.
6. You win by guessing the complete word before using all 6 attempts.

---

## 🎯 Learning Outcomes

This project helped me understand:

- Random word selection
- String manipulation
- List operations
- Loops and conditional statements
- User interaction with `input()`
- Basic game development in Python

---

## 🚀 Future Enhancements

- Add difficulty levels (Easy, Medium, Hard)
- Read words from an external text file
- Display Hangman ASCII art
- Add hints for each word
- Score tracking
- Multiple game rounds
- GUI version using Tkinter or Pygame

---

# Task2:- Stock Portfolio Tracker

A simple **Stock Portfolio Tracker** built using **Python** that allows users to calculate the total value of their stock investments based on predefined stock prices. The user enters stock names and quantities, and the program calculates the total investment value. It also saves the portfolio summary to a text file.

This project was developed as **Task 2** of the **CodeAlpha Python Programming Internship**.

---

## 📌 Features

- 📊 Uses a predefined dictionary of stock prices
- 📝 Accepts user input for stock names and quantities
- 💰 Calculates the investment value for each stock
- 📈 Displays the total portfolio value
- 💾 Saves the portfolio summary to a `portfolio.txt` file
- ❌ Handles invalid stock names gracefully

---

## 🛠️ Technologies Used

- Python 3.x

### Concepts Used
- Dictionary
- User Input & Output
- For Loops
- If-Else Statements
- Basic Arithmetic
- Lists
- File Handling (`open()`, `write()`)

---

## 📂 Project Structure

```
Stock-Portfolio-Tracker/
│── stock_portfolio.py
│── portfolio.txt
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/tejasjangid42-rgb/Stock-Portfolio-Tracker.git
```

2. Navigate to the project directory:

```bash
cd Stock-Portfolio-Tracker
```

3. Run the program:

```bash
python stock_portfolio.py
```

---

## 📋 Sample Input

```text
How many stocks do you want to enter? 2

Enter stock name: AAPL
Enter quantity: 10

Enter stock name: TSLA
Enter quantity: 5
```

---

## 📤 Sample Output

```text
📈 Stock Portfolio Tracker

Value of AAPL: $1800
Value of TSLA: $1250

📊 Portfolio Summary

AAPL, Quantity: 10, Value: $1800
TSLA, Quantity: 5, Value: $1250

💰 Total Investment Value: $3050

✅ Portfolio saved to 'portfolio.txt'
```

---

## 📖 How It Works

1. The program stores stock prices in a dictionary.
2. The user enters the number of different stocks.
3. The user provides the stock symbol and quantity.
4. The program calculates the value of each stock.
5. The total investment value is displayed.
6. A portfolio summary is saved to a text file.

---

## 🎯 Learning Outcomes

This project helped me gain practical experience in:

- Working with Python dictionaries
- Accepting and validating user input
- Using loops and conditional statements
- Performing arithmetic calculations
- File handling in Python
- Developing a simple finance-related application

---

## 🚀 Future Enhancements

- 📡 Fetch live stock prices using APIs
- 📄 Export portfolio to CSV or Excel
- 📊 Visualize portfolio with charts
- 📈 Calculate profit/loss percentages
- 🖥️ Build a GUI using Tkinter
- 💾 Store portfolio data in a database

---

# Task4:- Basic Chatbot

A simple **rule-based chatbot** built using **Python** that interacts with users through the command line. The chatbot responds to predefined user inputs such as greetings, common questions, and exit commands using conditional statements.

This project was developed as **Task 4** of the **CodeAlpha Python Programming Internship**.

---

## 📌 Features

- 💬 Interactive command-line chatbot
- 👋 Responds to greetings like **"hello"**
- 😊 Answers simple questions like **"how are you"**
- 🙋 Introduces itself when asked its name
- 👋 Ends the conversation when the user types **"bye"**
- ❓ Handles unknown inputs with a default response

---

## 🛠️ Technologies Used

- Python 3.x

### Concepts Used

- Functions
- While Loop
- If-Elif-Else Statements
- String Methods (`lower()`)
- User Input & Output

---

## 📂 Project Structure

```
Basic-Chatbot/
│── chatbot.py
│── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/tejasjangid42-rgb/Basic-Chatbot.git
```

2. Navigate to the project directory:

```bash
cd Basic-Chatbot
```

3. Run the program:

```bash
python chatbot.py
```

---

## 💬 Sample Conversation

```text
🤖 Chatbot: Hello! Type 'bye' to exit.

You: hello
🤖 Chatbot: Hi!

You: how are you
🤖 Chatbot: I'm fine, thanks!

You: what is your name
🤖 Chatbot: My name is SimpleBot.

You: bye
🤖 Chatbot: Goodbye!
```

---

## 📖 How It Works

1. The chatbot starts by greeting the user.
2. It continuously waits for user input.
3. User input is converted to lowercase for easier comparison.
4. The chatbot checks the input using `if-elif-else` conditions.
5. It responds with predefined messages.
6. Typing **"bye"** ends the conversation.

---

## 🎯 Learning Outcomes

This project helped me understand:

- Creating and using Python functions
- Implementing infinite loops with `while`
- Decision-making using `if-elif-else`
- Handling user input
- String manipulation with `lower()`
- Building a simple rule-based chatbot

---

## 🚀 Future Enhancements

- 🧠 Integrate AI or NLP for smarter conversations
- 🎤 Add voice input and speech output
- 🌐 Connect to APIs for real-time information
- 💾 Store conversation history
- 🖥️ Develop a GUI using Tkinter or PyQt
- 🤖 Add more intents and responses







