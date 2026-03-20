import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для Windows
init(autoreset=True)

def visualize_directory(path: Path, indent: str = ""):
    # Перевіряємо, чи шлях існує і чи це директорія
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує.")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не є директорією.")
        return

    # Виводимо корінь (тільки при першому виклику)
    if indent == "":
        print(f"{Fore.BLUE}{Style.BRIGHT}📦{path.name}")

    # Отримуємо всі елементи в директорії та сортуємо їх (спочатку папки, потім файли)
    items = sorted(list(path.iterdir()), key=lambda x: (x.is_file(), x.name.lower()))

    for i, item in enumerate(items):
        # Визначаємо, чи це останній елемент у списку для малювання символів гілок
        is_last = (i == len(items) - 1)
        connector = "┗ " if is_last else "┣ "
        
        if item.is_dir():
            # Виводимо папку синім кольором
            print(f"{indent}{connector}{Fore.CYAN}📂{item.name}")
            # Рекурсивний виклик для підпапки
            new_indent = indent + ("  " if is_last else "┃ ")
            visualize_directory(item, new_indent)
        else:
            # Виводимо файл зеленим кольором
            print(f"{indent}{connector}{Fore.GREEN}📜{item.name}")

def main():
    # Перевіряємо, чи передано аргумент командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Використання: python task_3.py <шлях_до_директорії>")
        return

    # Отримуємо шлях з аргументів
    target_path = Path(sys.argv[1])
    visualize_directory(target_path)

if __name__ == "__main__":
    main()


