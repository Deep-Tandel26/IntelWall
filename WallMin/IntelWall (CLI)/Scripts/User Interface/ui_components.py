from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel

# Initialize Rich console
console = Console()

def display_panel(title, content, border_style="cyan"):
    """Display a panel with a title and content."""
    console.print(Panel(content, title=title, border_style=border_style))

def get_input(prompt_text, is_password=False):
    """Get user input."""
    console.print(f"[bold yellow]{prompt_text}[/bold yellow]", end="")
    return prompt("", is_password=is_password).strip()