from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel

# Import validation and authentication directly from the respective files
from credentials_validation import validation
from User_Authentication import User_authorization

# Initialize Rich console
console = Console()

# Mock database for storing user data
user_database = {"admin": {"username": "admin", "password": "admin123"}, "users": []}

# Mock firewall rules database
firewall_rules = {"chains": {}, "tables": {}}

def display_panel(title, content, border_style="cyan"):
    """Display a panel with a title and content."""
    console.print(Panel(content, title=title, border_style=border_style))

def get_input_with_validation(prompt_text, validation_func, error_message, is_password=False):
    """Get user input and validate it dynamically."""
    while True:
        console.print(f"[bold yellow]{prompt_text}[/bold yellow]", end="")
        user_input = prompt("", is_password=is_password).strip()
        if validation_func(user_input):
            return user_input
        console.print(f"[bold red]{error_message}[/bold red]")

def manage_firewall_rules():
    """Manage firewall rules after authentication."""
    while True:
        display_panel(
            "Firewall Rules Management",
            "[bold yellow]1. Add Rule\n2. Delete Rule\n3. Modify Rule\n4. Review Rules\n5. Exit[/bold yellow]",
            "cyan"
        )
        console.print("[bold yellow]Enter action (1/2/3/4/5):[/bold yellow]", end="")
        action = prompt("").strip()
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
            console.print("[bold red]Invalid action. Please enter '1', '2', '3', '4', or '5'.[/bold red]")

def add_firewall_rule():
    """Add a new firewall rule."""
    chain = get_input_with_validation("Enter chain name:", lambda x: len(x) > 0, "Chain name cannot be empty.")
    table = get_input_with_validation("Enter table name:", lambda x: len(x) > 0, "Table name cannot be empty.")
    rule = get_input_with_validation("Enter rule details:", lambda x: len(x) > 0, "Rule details cannot be empty.")
    if chain not in firewall_rules["chains"]:
        firewall_rules["chains"][chain] = []
    if table not in firewall_rules["tables"]:
        firewall_rules["tables"][table] = []
    firewall_rules["chains"][chain].append(rule)
    firewall_rules["tables"][table].append(rule)
    display_panel("Success", f"Rule added to chain '{chain}' and table '{table}'.", "green")

def delete_firewall_rule():
    """Delete an existing firewall rule."""
    chain = get_input_with_validation("Enter chain name:", lambda x: x in firewall_rules["chains"], "Chain not found.")
    table = get_input_with_validation("Enter table name:", lambda x: x in firewall_rules["tables"], "Table not found.")
    rule = get_input_with_validation("Enter rule details to delete:", lambda x: x in firewall_rules["chains"][chain], "Rule not found in the specified chain.")
    firewall_rules["chains"][chain].remove(rule)
    firewall_rules["tables"][table].remove(rule)
    display_panel("Success", f"Rule removed from chain '{chain}' and table '{table}'.", "green")

def modify_firewall_rule():
    """Modify an existing firewall rule."""
    chain = get_input_with_validation("Enter chain name:", lambda x: x in firewall_rules["chains"], "Chain not found.")
    table = get_input_with_validation("Enter table name:", lambda x: x in firewall_rules["tables"], "Table not found.")
    old_rule = get_input_with_validation("Enter rule details to modify:", lambda x: x in firewall_rules["chains"][chain], "Rule not found in the specified chain.")
    new_rule = get_input_with_validation("Enter new rule details:", lambda x: len(x) > 0, "New rule details cannot be empty.")
    index = firewall_rules["chains"][chain].index(old_rule)
    firewall_rules["chains"][chain][index] = new_rule
    firewall_rules["tables"][table][index] = new_rule
    display_panel("Success", f"Rule modified in chain '{chain}' and table '{table}'.", "green")

def review_firewall_rules():
    """Review all firewall rules."""
    if not firewall_rules["chains"] and not firewall_rules["tables"]:
        display_panel("No Rules", "No firewall rules found.", "yellow")
        return
    content = "[bold cyan]Firewall Rules:[/bold cyan]\n"
    for chain, rules in firewall_rules["chains"].items():
        content += f"\n[bold yellow]Chain: {chain}[/bold yellow]\n"
        for rule in rules:
            content += f"- {rule}\n"
    for table, rules in firewall_rules["tables"].items():
        content += f"\n[bold yellow]Table: {table}[/bold yellow]\n"
        for rule in rules:
            content += f"- {rule}\n"
    display_panel("Firewall Rules", content, "cyan")

def login():
    """Handle the login process."""
    display_panel("IntelWall - Login", "Enter account type (admin/user):", "blue")
    account_type = get_input_with_validation(
        "> ",
        lambda x: x in ["admin", "user"],
        "Invalid account type. Please enter 'admin' or 'user'."
    )
    display_panel(f"{account_type.capitalize()} Login", "Enter your credentials:", "green")
    username = get_input_with_validation("Username:", lambda x: len(x) > 0, "Username cannot be empty.")
    password = get_input_with_validation("Password:", lambda x: len(x) > 0, "Password cannot be empty.", is_password=True)
    if account_type == "admin":
        valid = username == user_database["admin"]["username"] and password == user_database["admin"]["password"]
    else:
        valid = any(u for u in user_database["users"] if u["username"] == username and u["password"] == password)
    if valid:
        display_panel(
            "Welcome Back",
            f"[bold green]Welcome back, {username}! You can now manage your firewall rules.[/bold green]",
            "green",
        )
        manage_firewall_rules()
    else:
        display_panel("Error", "Invalid credentials. Please try again.", "red")

def signup():
    """Handle the signup process."""
    display_panel("IntelWall - Signup", "Enter your details:", "blue")
    validator = validation()
    name = get_input_with_validation("Name:", lambda x: len(x) > 0, "Name cannot be empty.")
    email = get_input_with_validation(
        "Email:",
        validator.email_validation,
        "Invalid email format. Please ensure the email contains '@' and '.' and starts with a letter or digit."
    )
    username = get_input_with_validation(
        "Username:",
        validator.username_validation,
        "Invalid username. Criteria:\n- 4-20 characters long\n- Alphanumeric or underscores only."
    )
    password = get_input_with_validation(
        "Password:",
        lambda x: len(x) >= 8,
        "Password must be at least 8 characters long.",
        is_password=True
    )
    confirm_password = get_input_with_validation(
        "Confirm Password:",
        lambda x: x == password,
        "Passwords do not match. Please try again.",
        is_password=True
    )
    if not validator.password_validation(password, confirm_password):
        display_panel("Error", "Password validation failed. Ensure it meets the criteria.", "red")
        return
    user_auth = User_authorization()
    user_details = user_auth.User_details()
    user_database["users"].append(user_details)
    display_panel("Success", "Signup successful! You can now log in.", "green")
    manage_firewall_rules()

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
        console.print("[bold yellow]Please select an option (1/2/3):[/bold yellow]", end="")
        action = prompt("").strip()
        if action == "1":
            login()
        elif action == "2":
            signup()
            display_panel(
                "Welcome New User",
                "[bold green]Thank you for signing up! You can now manage your firewall rules with IntelWall.[/bold green]",
                "green",
            )
        elif action == "3":
            display_panel("Goodbye", "[bold magenta]Thank you for using IntelWall![/bold magenta]", "magenta")
            break
        else:
            console.print("[bold red]Invalid option. Please enter '1', '2', or '3'.[/bold red]")

if __name__ == "__main__":
    main()

