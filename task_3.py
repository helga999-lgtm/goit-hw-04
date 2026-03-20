import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory(path: Path, indent: str = ""):

    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не є директорією.")
        return

    if indent == "":
        print(f"{Fore.BLUE}{Style.BRIGHT}📦{path.name}")

    items = sorted(list(path.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "┗ " if is_last else "┣ "
        
        if item.is_dir():
            print(f"{indent}{connector}{Fore.CYAN}📂{item.name}")
            new_indent = indent + ("  " if is_last else "┃ ")
            visualize_directory(item, new_indent)
        else:
            print(f"{indent}{connector}{Fore.GREEN}📜{item.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python task_3.py <шлях_до_директорії>")
        return

    target_path = Path(sys.argv[1])
    visualize_directory(target_path)

if __name__ == "__main__":
    main()


