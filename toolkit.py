"""
Personal Mini-Toolkit

Final Project - PLP Python Week 8

Author: [YOUR NAME]
Description: A menu-driven program with 4 useful tools in one place.
             The program keeps showing the menu until the user chooses to quit.

Tools:
    1. To-Do List Manager - Manage daily tasks
    2. Expense Tracker - Track spending and see total
    3. Grade Calculator - Convert a score to a grade
    4. Password Generator - Create a strong random password

Concepts Used:
    - Variables, Input/Output, Conditionals (if/elif/else)
    - Loops (while True, for loops)
    - Lists (that change while program runs)
    - f-strings for friendly messages
    - Functions to keep code organised
    - try/except to stop crashes from bad input

How To Run:
  python toolkit.py
"""

import random
import string

# ==========================================================
# DATA STORAGE
# These lists live outside the functions so they are not
# deleted when a tool finishes. They change while the
# program runs - this is why the program remembers your data.
# ==========================================================
todo_list = []          # Example: ["Do homework", "Buy milk"]
expense_names = []      # Example: ["Lunch", "Bus"]
expense_amounts = []    # Example: [5.50, 2.00]

def show_menu():
    """
    Show the main menu.
    This is the exact menu text from toolkit_plan.txt.
    """
    print("\n" + "=" * 40)
    print("   🧰  MY PERSONAL MINI-TOOLKIT")
    print("=" * 40)
    print("1. To-Do List Manager")
    print("2. Expense Tracker")
    print("3. Grade Calculator")
    print("4. Password Generator")
    print("5. Quit")
    print("=" * 40)

# ==========================================================
# TOOL 1: TO-DO LIST MANAGER
# What it does: Lets the user add tasks, view all tasks,
# and remove a task when it is finished.
# Concepts: LIST (todo_list changes with append/pop),
# LOOP (while + for), CONDITIONAL (if/elif/else),
# f-string for friendly output.
# ==========================================================
def todo_tool():
    print("\n--- ✅ TO-DO LIST MANAGER ---")
    print("Here you can organise your day. Add tasks and tick them off!")

    while True:
        print("\nTo-Do Menu:")
        print("a. Add a task")
        print("b. View all tasks")
        print("c. Remove a task")
        print("d. Back to Main Menu")
        choice = input("Choose a, b, c or d: ").lower().strip()

        if choice == "a":
            task = input("Enter your new task: ").strip()
            if task == "":
                print("⚠️ Oops! Task cannot be empty. Try again.")
            else:
                todo_list.append(task)
                print(f"✔️ Great! Added: '{task}'")
                print(f"You now have {len(todo_list)} task(s) in your list.")

        elif choice == "b":
            if len(todo_list) == 0:
                print("📭 Your to-do list is empty. Add a task first!")
            else:
                print("\n📋 Your Tasks:")
                for i, task in enumerate(todo_list, start=1):
                    print(f"  {i}. {task}")

        elif choice == "c":
            if len(todo_list) == 0:
                print("📭 Nothing to remove. Your list is already empty.")
            else:
                print("\nWhich task do you want to remove?")
                for i, task in enumerate(todo_list, start=1):
                    print(f"  {i}. {task}")
                try:
                    num = int(input("Enter number of task to remove: "))
                    if 1 <= num <= len(todo_list):
                        removed = todo_list.pop(num - 1)
                        print(f"🗑️ Well done! Removed: '{removed}'")
                        print(f"You now have {len(todo_list)} task(s) left.")
                    else:
                        print("⚠️ That number is not in the list.")
                except ValueError:
                    print("⚠️ Please enter a number, not letters.")

        elif choice == "d":
            print("👋 Going back to Main Menu. See you there!")
            break
        else:
            print("⚠️ Hmm, I didn't understand that. Please choose a, b, c or d.")

# ==========================================================
# TOOL 2: EXPENSE TRACKER
# What it does: Lets the user add expenses (what they bought
# and how much it cost) and shows the total spent.
# Concepts: TWO LISTS (names + amounts that grow together),
# LOOP (for loop to add total), CONDITIONAL (check negative
# amount), f-string to show money nicely like $5.50.
# ==========================================================
def expense_tool():
    print("\n--- 💰 EXPENSE TRACKER ---")
    print("Track where your money goes. Small spending adds up!")

    while True:
        print("\nExpense Menu:")
        print("a. Add an expense")
        print("b. View all expenses and total")
        print("c. Back to Main Menu")
        choice = input("Choose a, b or c: ").lower().strip()

        if choice == "a":
            name = input("What did you buy? ").strip()
            try:
                amount = float(input("How much did it cost? $ "))
                if amount < 0:
                    print("⚠️ Amount cannot be negative. Try again.")
                else:
                    expense_names.append(name)
                    expense_amounts.append(amount)
                    print(f"✔️ Added: {name} - ${amount:.2f}")
                    print("Nice, your expense has been saved!")
            except ValueError:
                print("⚠️ Please enter a valid number for amount, e.g. 5.50")

        elif choice == "b":
            if len(expense_names) == 0:
                print("📭 No expenses yet. Add your first expense!")
            else:
                print("\n🧾 Your Expenses:")
                total = 0
                for i in range(len(expense_names)):
                    print(f"  {i+1}. {expense_names[i]} - ${expense_amounts[i]:.2f}")
                    total += expense_amounts[i]
                print("-" * 30)
                print(f"💰 TOTAL SPENT: ${total:.2f}")
                print(f"You have {len(expense_names)} expense(s) recorded.")

        elif choice == "c":
            print("👋 Going back to Main Menu...")
            break
        else:
            print("⚠️ Invalid choice. Please choose a, b or c.")

# ==========================================================
# TOOL 3: GRADE CALCULATOR
# What it does: Takes a score from 0 to 100 and tells the
# user their grade: A, B, C, D, or F.
# Concepts: CONDITIONAL is the main concept here -
# a full if / elif / else chain. Also uses try/except
# so typing letters does not crash the program.
# ==========================================================
def grade_tool():
    print("\n--- 🎓 GRADE CALCULATOR ---")
    print("Enter your score and I will tell you your grade!")

    try:
        score = float(input("Enter your score (0 - 100): "))

        if score < 0 or score > 100:
            print(f"⚠️ Oops! {score} is not valid. Score must be between 0 and 100.")
        elif score >= 90:
            print(f"🎉 Amazing! Your score is {score} - Your grade is A - Excellent!")
        elif score >= 80:
            print(f"👏 Well done! Your score is {score} - Your grade is B - Very Good!")
        elif score >= 70:
            print(f"👍 Good job! Your score is {score} - Your grade is C - Good!")
        elif score >= 60:
            print(f"Your score is {score} - Your grade is D - You passed! You can do even better next time.")
        else:
            print(f"Your score is {score} - Your grade is F - Don't give up! Keep trying, you will improve.")
    except ValueError:
        print("⚠️ Please enter a number, e.g. 85")

# ==========================================================
# TOOL 4: PASSWORD GENERATOR
# What it does: Creates a random strong password.
# The user chooses how long it should be.
# Concepts: LOOP (for loop builds password one character
# at a time), CONDITIONAL (check length is at least 4),
# f-string, and the random + string libraries.
# ==========================================================
def password_tool():
    print("\n--- 🔐 PASSWORD GENERATOR ---")
    print("Need a strong password? I will make one for you!")

    try:
        length = int(input("How long should the password be? (e.g. 8, 12): "))
        if length < 4:
            print("⚠️ For safety, password should be at least 4 characters.")
        else:
            characters = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ""
            for i in range(length):
                password += random.choice(characters)
            print(f"\n🔑 Your new password is: {password}")
            print(f"It has {length} characters. Copy it and keep it safe!")
            print("Tip: Don't share your password with anyone.")
    except ValueError:
        print("⚠️ Please enter a number, e.g. 12")

# ==========================================================
# MAIN PROGRAM - THE MENU LOOP
# What it does: Shows the menu, asks for a choice, and
# uses if/elif/else to run the right tool. The while True
# loop makes the menu come back after every tool finishes.
# It only stops when the user chooses 5 (Quit).
# ==========================================================
def main():
    # WELCOMING START MESSAGE - Part D Requirement
    print("\n" + "=" * 50)
    print("  👋 WELCOME TO YOUR PERSONAL MINI-TOOLKIT! 👋")
    print("  I have 4 helpful tools for you today.")
    print("  Pick a number, try a tool, and have fun!")
    print("=" * 50)

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            todo_tool()
        elif choice == "2":
            expense_tool()
        elif choice == "3":
            grade_tool()
        elif choice == "4":
            password_tool()
        elif choice == "5":
            # FRIENDLY GOODBYE - Part D Requirement
            print("\n" + "=" * 50)
            print("  👋 Thank you for using the Mini-Toolkit!")
            print("  You did great today. Come back soon!")
            print("  Goodbye and have a wonderful day! ✨")
            print("=" * 50)
            break
        else:
            print("⚠️ Hmm, that's not on the menu. Please enter a number from 1 to 5.")
            print("Don't worry, the menu will show again!")

# Start the program - this line runs main() when you run the file
if __name__ == "__main__":
    main()
