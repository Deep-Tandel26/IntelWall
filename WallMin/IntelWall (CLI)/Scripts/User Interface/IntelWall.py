#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ui_components import display_panel, get_input
from Rules.Add.main import Add
from Rules.Modify.main import Modify
from Rules.Delete.main import Delete
from Rules.Review_and_Analyse.main import ReviewAndAnalyse

# Available nftables table options
NFTABLES_TABLES = ["filter", "nat", "mangle", "raw", "security"]

def authenticate_user():
    """Authenticate the user using PAM (commented out for now)."""
    display_panel("Authentication", "[bold green]Authentication is currently disabled.[/bold green]", "green")
    return "user"

def choose_table():
    """Ask the user to choose a table to work with."""
    display_panel(
        "Choose Table",
        "Please select the table you want to work with:\n" +
        "\n".join(f"[bold yellow]{i + 1}. {table}[/bold yellow]" for i, table in enumerate(NFTABLES_TABLES)),
        "cyan"
    )
    while True:
        choice = get_input("Enter the number corresponding to your choice:")
        if choice.isdigit() and 1 <= int(choice) <= len(NFTABLES_TABLES):
            return NFTABLES_TABLES[int(choice) - 1]
        else:
            display_panel("Error", "Invalid choice. Please select a valid table number.", "red")

def manage_table(table_name):
    """Manage the selected table."""
    chains = {}  # Initialize an empty dictionary to store chains and rules
    add = Add()
    modify = Modify(chains)
    delete = Delete(chains)
    review_and_analyse = ReviewAndAnalyse(chains)

    while True:
        display_panel(
            f"Managing Table: {table_name}",
            "[bold yellow]1. Add Chains and Rules\n2. Delete Chains and Rules\n"
            "3. Modify Chains and Rules\n4. Review and Analyse Policies , Chains and Rules\n5. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1-5):")
        if choice == "1":
            manage_add(add, table_name)
        elif choice == "2":
            manage_delete(delete, table_name)
        elif choice == "3":
            manage_modify(modify, table_name)
        elif choice == "4":
            manage_review_and_analyse(review_and_analyse, table_name)
        elif choice == "5":
            display_panel("Exit", f"[bold magenta]Exiting table '{table_name}' management...[/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")

def manage_add(add, table_name):
    """Manage adding chains and rules."""
    while True:
        display_panel(
            "Add Policies and Rules",
            "[bold yellow]1. Add Chain\n2. Add Rule\n3. Back[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1-3):")
        if choice == "1":
            display_panel("Add Chain", f"Adding a new chain to the table [bold green]'{table_name}'[/bold green].", "cyan")
            output = add.add_chain(table_name)
            display_panel("Add Chain Output", output, "green")
        elif choice == "2":
            display_panel("Add Rule", f"Adding a new rule to the table [bold green]'{table_name}'[/bold green].", "cyan")
            output = add.add_rule()
            display_panel("Add Rule Output", output, "green")
        elif choice == "3":
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")

def manage_delete(delete, table_name):
    """Manage deleting chains and rules."""
    while True:
        display_panel(
            "Delete Policies and Rules",
            "[bold yellow]1. Delete Chain\n2. Delete Rule\n3. Back[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1-3):")
        if choice == "1":
            display_panel("Delete Chain", f"Deleting a chain from the table '{table_name}'.", "cyan")
            output = delete.delete_chain()
            display_panel("Delete Chain Output", output, "green")
        elif choice == "2":
            display_panel("Delete Rule", f"Deleting a rule from the table '{table_name}'.", "cyan")
            output = delete.delete_rule()
            display_panel("Delete Rule Output", output, "green")
        elif choice == "3":
            break
        else:
            display_panel("Error", "Invalid choice. Please try again.", "red")

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
        "IntelWall is your trusted partner for robust, scalable, and intelligent firewall management.",
        "cyan",
    )

    # Simulate login or signup
    while True:
        display_panel(
            "IntelWall",
            "[bold cyan]Are you an Existing User?[/bold cyan]\n"
            "[bold yellow]1. Yes (Login)\n2. No (Signup)\n3. Exit[/bold yellow]",
            "cyan",
        )
        action = get_input("Please select an option (1/2/3):")
        if action == "1":
            username = authenticate_user()
            break
        elif action == "2":
            display_panel("Signup", "[bold green]Signup functionality will be implemented in the future.[/bold green]", "green")
        elif action == "3":
            display_panel("Goodbye", "[bold magenta]Thank you for using IntelWall![/bold magenta]", "magenta")
            return
        else:
            display_panel("Error", "Invalid option. Please enter '1', '2', or '3'.", "red")

    # Ask the user to choose a table
    table_name = choose_table()
    manage_table(table_name)

if __name__ == "__main__":
    main()

