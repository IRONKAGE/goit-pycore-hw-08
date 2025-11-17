import sys

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return None
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].upper(),
        "message": parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Помилка: файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return list(filter(lambda log: log["level"] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<16}| {counts[level]}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <шлях_до_лог_файлу> [рівень_логування]")
        sys.exit(1)

    log_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_path)
    counts = count_logs_by_level(logs)
    
    display_log_counts(counts)
    
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nНемає записів для рівня '{level_filter.upper()}'.")

if __name__ == "__main__":
    main()
