<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=Hangman%20Game&fontSize=48&fontColor=ffffff&animation=fadeIn&desc=CodeAlpha%20Python%20Internship%20%7C%20Task%201&descSize=18&descAlignY=72" width="100%" alt="Hangman Game"/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=for-the-badge)
![Task](https://img.shields.io/badge/Task-1-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

### 🎯 Guess the hidden word before you run out of chances!

</div>

---

## 📌 About the Project

The **Hangman Game** is a classic word-guessing challenge built in Python as **Task 1** of my **CodeAlpha Python Programming Internship**.

In this console-based version, the program picks a **random hidden word**, and the player must uncover it **one letter at a time**. With a strict limit of **6 incorrect guesses**, every choice counts!

---

## 🎮 How to Play

1. The game chooses a random word from a predefined list.
2. The word is shown as blanks, for example `_ _ _ _ _ _`.
3. Guess **one letter** at a time.
4. A correct letter is revealed in its place in the word.
5. A wrong letter costs you **1 of your 6 chances**.
6. 🏆 **Win** by guessing the whole word. 💀 **Lose** if you run out of chances.

---

## ✨ Features

| | Feature |
|---|---|
| 🎲 | Picks a **random word** from a list of 5 predefined words |
| ⌨️ | Simple **console input/output**, no graphics or audio needed |
| ❤️ | Limit of **6 incorrect guesses** |
| 🔤 | Shows the word progress after every guess |
| 🔁 | Runs in a loop until the player wins or loses |
| 🏁 | Clear **win / lose** message at the end |

---

## 🛠️ Concepts Used

| Concept | Where it is used |
|---|---|
| `random` module | Choosing the hidden word |
| `while` loop | Keeping the game running |
| `if` - `else` | Checking correct and wrong guesses |
| Strings | Handling the word and each letter |
| Lists | Storing words and guessed letters |
| `input()` / `print()` | Talking to the player |

---

## 🚀 How to Run

1. Install **Python 3** on your system.
2. Download this repository (**Code → Download ZIP**) and extract it.
3. Open `hangman.py` in **IDLE** (or any Python editor) and press **F5** to run it.
4. Start guessing letters!

> No extra libraries need to be installed.

---

## 💻 Sample Gameplay

```text
===== HANGMAN GAME =====
Word: _ _ _ _ _ _
Enter a letter: a
Good guess!
Word: _ a _ _ _ _
Enter a letter: z
Wrong guess! Chances left: 5
...
Congratulations! You guessed the word!
```

> The exact messages may look slightly different when you run the game.

---

## 📁 Project Structure

```text
CodeAlpha_HangmanGame/
├── hangman.py      # main game program
└── README.md       # project documentation
```

---

## 👨‍💻 Author

**Arijit**
Python Programming Intern @ **CodeAlpha**

---

<div align="center">

⭐ **If you like this project, give it a star!** ⭐

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%" alt=""/>

</div>
