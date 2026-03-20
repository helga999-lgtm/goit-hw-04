def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:  
                    continue
                
                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у форматі даних рядка: '{line}'")
                    continue
        
        if count == 0:
            return 0, 0
        
        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Виникла непередбачувана помилка: {e}")
        return None, None

total, average = total_salary(r"C:\GoIT\Git\modul4\Go_IT_4\salary_file.txt")

if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")