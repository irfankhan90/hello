#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TO-DO LIST project

tasks = []

def display_tasks():
    print("TO-DO LIST:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    display_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if task_number >= 0 and task_number < len(tasks):
        del tasks[task_number]
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# In[1]:


#CALCULATOR

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = int(input("Enter operation choice (1-4): "))

if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
        exit()
else:
    print("Invalid choice!")
    exit()

print("Result:", result)



# In[2]:


# PASSWORD GENERATOR

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()



# In[6]:


#Rock-Paper-Scissors game 

import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_score = 0
    user_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in choices:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

        computer_choice = random.choice(choices)
        print(f"\nComputer chose: {computer_choice}")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1

        print(f"\nScore - You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()

        if play_again != "yes":
            break

play_game()


# In[7]:


# Contact Book  


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully!")

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        for name, details in self.contacts.items():
            if search_term in [name, details["phone"]]:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    def update_contact(self):
        name = input("Enter name of contact to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name of contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# In[ ]:




