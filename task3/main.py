import sys
from pathlib import Path
from collections import Counter

logfile = Path("logfile.log")

def load_logs(file_path: str) -> list:
    logs_list = []
    try:
        with open(file_path,"r",encoding="utf-8") as file: #відкриваємо файл
            for line in file:
                line = line.strip()
                if line:
                    parsed = parse_log_line(line)   
                    logs_list.append(parsed) #додаємо у список
            return logs_list
    except FileNotFoundError: #якщо файл не існує
        print("File not found.")
        return []
    return logs_list

def parse_log_line(line: str) -> dict:
    parts = line.split(maxsplit=3) #розділяємо рядок на частини
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}

def filter_logs_by_level(logs: list, level: str) -> list: #фільтруємо
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict: #підраховуємо
    levels = [log['level'] for log in logs]
    return Counter(levels)

def display_log_counts(counts: dict): #виводимо
    print(f"{'Рівень логування':<17} | {'Кількість':<10}")
    print("-" * 18 + "|" + "-" * 11)
    for level, count in counts.items():
        print(f"{level:<17} | {count:<10}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_файлу> [рівень]")
        return

    path = sys.argv[1]
    logs = load_logs(path)
    
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()