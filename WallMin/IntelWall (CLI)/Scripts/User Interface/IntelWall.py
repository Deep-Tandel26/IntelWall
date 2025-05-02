#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import random
import string
# from simplepam import authenticate  # Uncomment this line to enable PAM authentication
from ui_components import display_panel, get_input
from Rules.Add.main import Add
from Rules.Modify.main import Modify
from Rules.Delete.main import Delete
from Rules.Review_and_Analyse.main import ReviewAndAnalyse

# Available nftables table options
NFTABLES_TABLES = ["filter", "nat", "mangle", "raw", "security"]

class User:
    def __init__(self, username):
        """
        Initialize a user with a unique JSON file to store chains and rules.
        :param username: The username of the user.
        """
        self.username = username
        self.user_id = self.generate_unique_id()
        self.filepath = f"{self.user_id}.json"
        self.data = self.load_user_data()

    def generate_unique_id(self):
        """Generate a random 16-character alphanumeric ID."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def load_user_data(self):
        """Load user data from the JSON file or initialize a new structure."""
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        else:
            return {"username": self.username, "chains": {}}

    def save_user_data(self):
        """Save the user's chains and rules to the JSON file."""
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)

def authenticate_user():
    """
    Authenticate the user using PAM or create a new user.
    PAM authentication is currently commented out.
    """
    # Uncomment the following block to enable PAM authentication
    """
    while True:
        display_panel("Authentication", "[bold cyan]Welcome to IntelWall[/bold cyan]\n\nEnter your credentials to proceed:\nUsername: ________\nPassword: ________", "cyan")
        username = get_input("Username: ")
        password = get_input("Password: ", is_password=True)
        if authenticate(username, password):
            display_panel("Authentication Successful", f"[bold green]Welcome, {username}![/bold green]", "green")
            return User(username)
        else:
            display_panel("Authentication Failed", "[bold red]Invalid username or password. Please try again.[/bold red]", "red")
    """
    # Fallback to simple username-based authentication for now
    display_panel("Authentication", "[bold cyan]Welcome to IntelWall![/bold cyan]\n\nEnter your username to proceed:", "cyan")
    username = get_input("[bold yellow]Username: [/bold yellow]")
    return User(username)

def choose_table():
    """Ask the user to choose a table to work with."""
    display_panel(
        "Choose Table",
        "[bold cyan]Please select the table you want to work with:[/bold cyan]\n" +
        "\n".join(f"[bold yellow]{i + 1}. {table}[/bold yellow]" for i, table in enumerate(NFTABLES_TABLES)) +
        "\n[bold yellow]0. Back[/bold yellow]",
        "cyan",
        level="1.1"  # Level 1.1: Choosing a table
    )
    while True:
        choice = get_input("[bold yellow]Enter the number corresponding to your choice: [/bold yellow]")
        if choice == "0":
            return None  # Go back to the previous step
        elif choice.isdigit() and 1 <= int(choice) <= len(NFTABLES_TABLES):
            return NFTABLES_TABLES[int(choice) - 1]
        else:
            display_panel("Invalid Input", "[bold red]Please select a valid table number from the menu.[/bold red]", "red", level="1.1")

def manage_table(user, table_name):
    """Manage the selected table for the user."""
    add = Add(user.data["chains"])
    modify = Modify(user.data["chains"])
    delete = Delete(user.data["chains"])
    review_and_analyse = ReviewAndAnalyse(user.data["chains"])

    while True:
        display_panel(
            f"Managing Table: {table_name}",
            "[bold cyan]Please select an action:[/bold cyan]\n"
            "[bold yellow]1. Add Chains and Rules\n2. Delete Chains and Rules\n"
            "3. Modify Chains and Rules\n4. Review and Analyse Policies and Rules\n5. Back[/bold yellow]",
            "cyan",
            level="2.1"  # Level 2.1: Managing a table
        )
        choice = get_input("[bold yellow]Enter your choice (1-5): [/bold yellow]")
        if choice == "1":
            manage_add(add, table_name)
        elif choice == "2":
            manage_delete(delete, table_name)
        elif choice == "3":
            manage_modify(modify, table_name)
        elif choice == "4":
            manage_review_and_analyse(review_and_analyse, table_name)
        elif choice == "5":
            user.save_user_data()
            break  # Go back to the previous step
        else:
            display_panel("Invalid Input", "[bold red]Please select a valid option from the menu.[/bold red]", "red", level="2.1")

def manage_add(add, table_name):
    """Manage adding chains and rules."""
    while True:
        display_panel(
            "Add Policies and Rules",
            "[bold cyan]Please select an action:[/bold cyan]\n"
            "[bold yellow]1. Add Chain\n2. Add Rule\n3. Back[/bold yellow]",
            "cyan",
            level="2.1.1"  # Level 2.1.1: Adding chains and rules
        )
        choice = get_input("[bold yellow]Enter your choice (1-3): [/bold yellow]")
        if choice == "1":
            display_panel("Add Chain", f"[bold cyan]Adding a new chain to the table '{table_name}'.[/bold cyan]", "cyan", level="2.1.1.1")
            output = add.add_chain(table_name)
            display_panel("Add Chain Output", f"[bold green]{output}[/bold green]", "green", level="2.1.1.1")
        elif choice == "2":
            display_panel("Add Rule", f"[bold cyan]Adding a new rule to the table '{table_name}'.[/bold cyan]", "cyan", level="2.1.1.2")
            output = add.add_rule()
            display_panel("Add Rule Output", f"[bold green]{output}[/bold green]", "green", level="2.1.1.2")
        elif choice == "3":
            break  # Go back to the previous step
        else:
            display_panel("Invalid Input", "[bold red]Please select a valid option from the menu.[/bold red]", "red", level="2.1.1")

def manage_delete(delete, table_name):
    """Manage deleting chains and rules."""
    while True:
        display_panel(
            "Delete Policies and Rules",
            "Please select an action:\n"
            "1. Delete Chain\n2. Delete Rule\n3. Back",
            "cyan",
            level="2.1.2"  # Level 2.1.2: Deleting chains and rules
        )
        choice = get_input("Enter your choice (1-3): ")
        if choice == "1":
            display_panel("Delete Chain", f"Deleting a chain from the table '{table_name}'.", "cyan", level="2.1.2.1")
            output = delete.delete_chain()
            display_panel("Delete Chain Output", output, "green", level="2.1.2.1")
        elif choice == "2":
            display_panel("Delete Rule", f"Deleting a rule from the table '{table_name}'.", "cyan", level="2.1.2.2")
            output = delete.delete_rule()
            display_panel("Delete Rule Output", output, "green", level="2.1.2.2")
        elif choice == "3":
            break  # Go back to the previous step
        else:
            display_panel("Invalid Input", "Please select a valid option from the menu.", "red", level="2.1.2")

def manage_modify(modify, table_name):
    """Manage modifying chains and rules."""
    while True:
        display_panel(
            "Modify Policies and Rules",
            "[bold yellow]1. Modify Chain\n2. Modify Rule\n3. Back[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1-3):")
        if choice == "1":
            display_panel("Modify Chain", f"Modifying a chain in the table '{table_name}'.", "cyan")
            output = modify.modify_chain()
            display_panel("Modify Chain Output", output, "green")
        elif choice == "2":
            display_panel("Modify Rule", f"Modifying a rule in the table '{table_name}'.", "cyan")
            output = modify.modify_rule()
            display_panel("Modify Rule Output", output, "green")
        elif choice == "3":
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")

def manage_review_and_analyse(review_and_analyse, table_name):
    """Manage reviewing and analyzing chains and rules."""
    while True:
        display_panel(
            "Review and Analyse Policies and Rules",
            "[bold yellow]1. Review Chains and Rules\n2. Analyze Chains and Rules\n3. Back[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1-3):")
        if choice == "1":
            display_panel("Review Chains and Rules", f"Reviewing chains and rules in the table '{table_name}'.", "cyan")
            output = review_and_analyse.review_chains_and_rules()
            display_panel("Review Chains and Rules Output", output, "cyan")
        elif choice == "2":
            display_panel("Analyze Chains and Rules", f"Analyzing chains and rules in the table '{table_name}'.", "cyan")
            output = review_and_analyse.analyse_chains_and_rules()
            display_panel("Analyze Chains and Rules Output", output, "cyan")
        elif choice == "3":
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")

def main():
    """Main function to display the interface."""
    display_panel(
        "Welcome to IntelWall",
        "[bold cyan]IntelWall[/bold cyan] is an intelligent, context-aware firewall rules manager designed for Linux.\n\n"
        "With IntelWall, you can:\n"
        "- [bold yellow]Easily configure and manage firewall rules[/bold yellow] for enhanced security.\n"
        "- [bold yellow]Monitor network traffic[/bold yellow] and detect anomalies in real-time.\n"
        "- [bold yellow]Gain actionable insights[/bold yellow] to develop secure and effective firewall policies.\n\n"
        "[bold cyan]IntelWall is your trusted partner for robust, scalable, and intelligent firewall management.[/bold cyan]",
        "cyan",
        level="1"  # Level 1: Main menu
    )

    # Authenticate or create a new user
    user = authenticate_user()

    while True:
        # Ask the user to choose a table
        table_name = choose_table()
        if table_name is None:
            break  # Exit the tool

        # Manage the selected table
        manage_table(user, table_name)

if __name__ == "__main__":
    main()

