#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ui_components import display_panel, get_input

# Mock firewall rules database
firewall_rules = {"chains": {}, "tables": {}}

def manage_firewall_rules():
    """Manage firewall rules."""
    while True:
        display_panel(
            "Firewall Rules Management",
            "[bold yellow]1. Add Rule\n2. Delete Rule\n3. Modify Rule\n4. Review Rules\n5. Exit[/bold yellow]",
            "cyan"
        )
        action = get_input("Enter action (1/2/3/4/5):")
        if action == "1":
            add_firewall_rule()
        elif action == "2":
            delete_firewall_rule()
        elif action == "3":
            modify_firewall_rule()
        elif action == "4":
            review_firewall_rules()
        elif action == "5":
            display_panel("Exit", "[bold magenta]Returning to main menu...[/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid action. Please enter '1', '2', '3', '4', or '5'.", "red")

def add_firewall_rule():
    """Add a new firewall rule."""
    chain = get_input("Enter chain name:")
    table = get_input("Enter table name:")
    rule = get_input("Enter rule details:")
    firewall_rules["chains"].setdefault(chain, []).append(rule)
    firewall_rules["tables"].setdefault(table, []).append(rule)
    display_panel("Success", f"Rule added to chain '{chain}' and table '{table}'.", "green")

def delete_firewall_rule():
    """Delete an existing firewall rule."""
    chain = get_input("Enter chain name:")
    table = get_input("Enter table name:")
    rule = get_input("Enter rule details to delete:")
    if chain in firewall_rules["chains"] and rule in firewall_rules["chains"][chain]:
        firewall_rules["chains"][chain].remove(rule)
    if table in firewall_rules["tables"] and rule in firewall_rules["tables"][table]:
        firewall_rules["tables"][table].remove(rule)
    display_panel("Success", f"Rule removed from chain '{chain}' and table '{table}'.", "green")

def modify_firewall_rule():
    """Modify an existing firewall rule."""
    chain = get_input("Enter chain name:")
    table = get_input("Enter table name:")
    old_rule = get_input("Enter rule details to modify:")
    new_rule = get_input("Enter new rule details:")
    if chain in firewall_rules["chains"] and old_rule in firewall_rules["chains"][chain]:
        index = firewall_rules["chains"][chain].index(old_rule)
        firewall_rules["chains"][chain][index] = new_rule
    if table in firewall_rules["tables"] and old_rule in firewall_rules["tables"][table]:
        index = firewall_rules["tables"][table].index(old_rule)
        firewall_rules["tables"][table][index] = new_rule
    display_panel("Success", f"Rule modified in chain '{chain}' and table '{table}'.", "green")

def review_firewall_rules():
    """Review all firewall rules."""
    if not firewall_rules["chains"] and not firewall_rules["tables"]:
        display_panel("No Rules", "No firewall rules found.", "yellow")
        return
    content = "[bold cyan]Firewall Rules:[/bold cyan]\n"
    for chain, rules in firewall_rules["chains"].items():
        content += f"\n[bold yellow]Chain: {chain}[/bold yellow]\n" + "\n".join(f"- {rule}" for rule in rules)
    for table, rules in firewall_rules["tables"].items():
        content += f"\n[bold yellow]Table: {table}[/bold yellow]\n" + "\n".join(f"- {rule}" for rule in rules)
    display_panel("Firewall Rules", content, "cyan")

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
    while True:
        display_panel(
            "IntelWall",
            "[bold cyan]Are you an Existing User?[/bold cyan]\n"
            "[bold yellow]1. Yes (Login)\n2. No (Signup)\n3. Exit[/bold yellow]",
            "cyan",
        )
        action = get_input("Please select an option (1/2/3):")
        if action == "1":
            display_panel("Login", "[bold green]Login functionality will be handled by PAM in the future.[/bold green]", "green")
            manage_firewall_rules()
        elif action == "2":
            display_panel("Signup", "[bold green]Signup functionality will be handled by PAM in the future.[/bold green]", "green")
        elif action == "3":
            display_panel("Goodbye", "[bold magenta]Thank you for using IntelWall![/bold magenta]", "magenta")
            break
        else:
            display_panel("Error", "Invalid option. Please enter '1', '2', or '3'.", "red")

if __name__ == "__main__":
    main()

