from pathlib import Path

base_path = Path('./Go_IT_4')

def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_data = line.split(',')
                    if len(cat_data) == 3:
                        cat_dict = {
                            "id": cat_data[0],
                            "name": cat_data[1],
                            "age": cat_data[2]
                        }
                        cats_list.append(cat_dict)
                        
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла неочікувана помилка: {e}")
        return []
        
    return cats_list

full_path = base_path / 'cats_file.txt'
cats_info = get_cats_info(full_path)

print("[")
for cat in cats_info:
    print(f"    {cat},")
print("]")