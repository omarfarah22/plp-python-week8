# Personal Mini-Toolkit 🧰

## Project Title
Personal Mini-Toolkit - PLP Python Week 8 Final Project

## What Does My Toolkit Do?

My Personal Mini-Toolkit is a menu-driven Python program that brings four useful tools together in one place. When you run the program, you see a numbered menu and you can choose a tool, use it, and then come back to the menu to try another one. The program keeps running until you choose Quit.

The four tools are:

### 1. To-Do List Manager ✅
Lets you add tasks, view all your tasks in a numbered list, and remove a task when you finish it. Your tasks are stored in a list that grows and shrinks while the program runs.

### 2. Expense Tracker 💰
Lets you add expenses by entering what you bought and how much it cost. It stores your expenses in two lists and shows you a full list plus your total amount spent.

### 3. Grade Calculator 🎓
Lets you enter a score from 0 to 100 and tells you your grade (A, B, C, D, or F) using if / elif / else conditionals, with a friendly encouraging message for each grade.

### 4. Password Generator 🔐
Lets you choose a length (e.g. 8 or 12) and creates a random strong password using letters, numbers, and symbols.

All tools use f-strings to give clear, friendly messages, and the program never crashes if you type a wrong choice or a letter instead of a number - it shows a polite message and shows the menu again.

## How To Run It

You need Python 3 installed on your computer. No other libraries are needed.

ReflectionThe hardest part for me was getting the menu loop to work correctly. I understood how to write one tool on its own, but making the main menu return after every tool finished, and only stop when the user chose Quit, took me a while to get right. The bug that took the longest to fix was when I typed a letter instead of a number for the grade calculator and the whole program crashed. I had to learn to use try/except to catch that error and show a friendly message instead of letting the program stop. I also struggled at first with the to-do list because I forgot that list numbers start at 0, so removing task 1 was actually removing index 0. Once I understood that, it made sense. If I had one more week, I would add a save feature so tasks and expenses are saved to a file and still there when you close and reopen the program. I would also add a fifth tool - a number-guessing game - and let the user save their favourite passwords. Overall, this project taught me that planning first in toolkit_plan.txt made building the code twice as fast, and testing every path helped me find bugs before submitting
