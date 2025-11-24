# vcs/ui.py
from rich.console import Console

console = Console()

def success(msg: str):
    console.print(f"✅ [bold green]{msg}[/bold green]")

def info(msg: str):
    console.print(f"[cyan]{msg}[/cyan]")

def warning(msg: str):
    console.print(f"⚠️ [yellow]{msg}[/yellow]")

def error(msg: str):
    console.print(f"❌ [bold red]{msg}[/bold red]")
