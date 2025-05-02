from prompt_toolkit import prompt
from rich.console import Console
from rich.panel import Panel
from rich.align import Align

# Initialize Rich console
console = Console()

def display_panel(title, content, color, level=None):
    """
    Display a panel with the given title, content, and color.
    Optionally, display the current hierarchy level at the bottom-right corner.
    """
    footer = f"[bold {color}]Level: {level}[/bold {color}]" if level else ""
    panel_content = f"{content}\n\n{footer}" if footer else content
    panel = Panel(
        Align.left(panel_content),
        title=f"[bold {color}]{title}[/bold {color}]",
        border_style=color,
    )
    console.print(panel)

def get_input(prompt_text, is_password=False):
    """Get user input."""
    console.print(f"[bold yellow]{prompt_text}[/bold yellow]", end="")
    return prompt("", is_password=is_password).strip()