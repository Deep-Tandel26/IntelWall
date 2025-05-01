#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from ui_components import display_panel, get_input
from collections import defaultdict
# from simplepam import authenticate  # Commented out for now
from Rules.Add.main import Add  # Corrected import for Add class from main.py

# Mock firewall rules database
firewall_rules = defaultdict(lambda: defaultdict(list))

# Available nftables table options
NFTABLES_TABLES = ["filter", "nat", "mangle", "raw", "security"]

def authenticate_user():
    """Authenticate the user using PAM (commented out for now)."""
    # while True:
    #     username = get_input("Enter your username:")
    #     password = get_input("Enter your password:", is_password=True)
    #     if authenticate(username, password):
    #         display_panel("Authentication Successful", f"[bold green]Welcome, {username}![/bold green]", "green")
    #         return username
    #     else:
    #         display_panel("Authentication Failed", "[bold red]Invalid username or password. Please try again.[/bold red]", "red")
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
    add = Add()  # Create an instance of the Add class from main.py
    while True:
        display_panel(
            f"Managing Table: {table_name}",
            "[bold yellow]1. Add Chain\n2. Add Rule\n3. Display Chains and Rules\n4. Exit[/bold yellow]",
            "cyan"
        )
        choice = get_input("Enter your choice (1/2/3/4):")
        if choice == "1":
            display_panel(
                "Add Chain",
                f"Adding a new chain to the table '{table_name}'.\nPlease follow the prompts.",
                "cyan"
            )
            chain_name = get_input("Enter the name of the chain:")
            table_name = get_input("Enter the table name (e.g., 'filter', 'nat'):")
            hook = get_input("Enter the hook (e.g., 'input', 'output', 'forward'):")
            priority = get_input("Enter the priority (e.g., '0', '-1'):")
            policy = get_input("Enter the policy (e.g., 'accept', 'drop'):")
            add.add_chain(chain_name, table_name, hook, priority, policy)
        elif choice == "2":
            display_panel(
                "Add Rule",
                f"Adding a new rule to the table '{table_name}'.\nPlease follow the prompts.",
                "cyan"
            )
            chain_name = get_input("Enter the chain name to add the rule to:")
            if chain_name not in add.chains:
                display_panel("Error", f"Chain '{chain_name}' does not exist. Please add the chain first.", "red")
            else:
                display_panel(
                    "Rule Types",
                    "Select the type of rule you want to add:\n"
                    "[bold yellow]1. Basic Rules\n2. IP-Based Rules\n3. Port-Based Rules\n"
                    "4. Logging and Monitoring Rules\n5. Stateful Rules\n6. Rate Limiting Rules\n7. Advanced Rules[/bold yellow]",
                    "cyan"
                )
                rule_type = get_input("Enter the number corresponding to the rule type:")
                add.add_rule(chain_name, rule_type)
        elif choice == "3":
            display_panel(
                "Display Chains and Rules",
                f"Displaying all chains and rules in the table '{table_name}'.",
                "cyan"
            )
            add.display_chains_and_rules()
        elif choice == "4":
            display_panel("Exit", f"[bold magenta]Exiting table '{table_name}' management...[/bold magenta]", "magenta")
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

