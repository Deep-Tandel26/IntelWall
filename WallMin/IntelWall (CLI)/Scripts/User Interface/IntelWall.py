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
    display_panel("Success" if valid else "Error", "Login successful!" if valid else "Invalid credentials.", "green" if valid else "red")

def signup():
    """Handle the signup process."""
    display_panel("IntelWall - Signup", "Enter your details:", "blue")
    validator = validation()
    name = get_input_with_validation("Name:", lambda x: len(x) > 0, "Name cannot be empty.")
    email = get_input_with_validation(
        "Email:",
        validator.email_validation,
        "Invalid email format. Please ensure the email contains '@' and '.' and starts with a letter or digit.Enter again."
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
        display_panel("IntelWall", "[bold yellow]1. Login\n2. Signup\n3. Exit[/bold yellow]", "cyan")
        console.print("[bold yellow]Enter action (1/2/3):[/bold yellow]", end="")
        action = prompt("").strip()
        if action == "1":
            login()
        elif action == "2":
            signup()
        elif action == "3":
            display_panel("Goodbye", "[bold magenta]Thank you for using IntelWall![/bold magenta]", "magenta")
            break
        else:
            console.print("[bold red]Invalid action. Please enter '1', '2', or '3'.[/bold red]")

if __name__ == "__main__":
    main()

