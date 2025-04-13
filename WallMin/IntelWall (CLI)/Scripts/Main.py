from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialize Rich console
console = Console()

# Sample firewall rules
firewall_rules = [
    {"id": 1, "action": "Allow", "protocol": "TCP", "port": 80, "description": "HTTP traffic"},
    {"id": 2, "action": "Deny", "protocol": "UDP", "port": 53, "description": "DNS traffic"},
]

def display_rules():
    """Display the current firewall rules in a table."""
    table = Table(title="Firewall Rules")
    table.add_column("ID", justify="center")
    table.add_column("Action", justify="center")
    table.add_column("Protocol", justify="center")
    table.add_column("Port", justify="center")
    table.add_column("Description", justify="left")

    for rule in firewall_rules:
        table.add_row(
            str(rule["id"]),
            rule["action"],
            rule["protocol"],
            str(rule["port"]),
            rule["description"]
        )

    console.print(table)

def add_rule():
    """Add a new firewall rule."""
    action_completer = WordCompleter(["Allow", "Deny"], ignore_case=True)
    protocol_completer = WordCompleter(["TCP", "UDP"], ignore_case=True)

    action = prompt("Enter action (Allow/Deny): ", completer=action_completer)
    protocol = prompt("Enter protocol (TCP/UDP): ", completer=protocol_completer)
    port = prompt("Enter port: ")
    description = prompt("Enter description: ")

    new_rule = {
        "id": len(firewall_rules) + 1,
        "action": action.capitalize(),
        "protocol": protocol.upper(),
        "port": int(port),
        "description": description
    }

    firewall_rules.append(new_rule)
    console.print(Text("Firewall rule added successfully!", style="bold green"))

def remove_rule():
    """Remove a firewall rule."""
    rule_id = prompt("Enter the ID of the rule to remove: ")
    global firewall_rules
    firewall_rules = [rule for rule in firewall_rules if rule["id"] != int(rule_id)]
    console.print(Text("Firewall rule removed successfully!", style="bold green"))

def main():
    """Main interactive CLI loop."""
    while True:
        console.print("\n[bold cyan]Firewall Rules Manager[/]")
        console.print("1. Display Firewall Rules")
        console.print("2. Add Firewall Rule")
        console.print("3. Remove Firewall Rule")
        console.print("4. Exit\n")

        choice = prompt("Select an option (1-4): ")

        if choice == "1":
            display_rules()
        elif choice == "2":
            add_rule()
        elif choice == "3":
            remove_rule()
        elif choice == "4":
            console.print(Text("Goodbye!", style="bold magenta"))
            break
        else:
            console.print(Text("Invalid option. Please try again.", style="bold red"))

if __name__ == "__main__":
    main()