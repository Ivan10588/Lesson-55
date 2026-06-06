import json
from pathlib import Path
from typing import Union

FilePath = Union[str, Path]

def update_queue_log(file_path, remaining):
    """Обновляет JSON-лог с количеством оставшихся страниц и выводит статус в консоль.

    Args:
        file_path (str): Путь к файлу лога (JSON).
        remaining (int): Количество оставшихся страниц в очереди.
    """
    with open(file_path, 'w') as f:
        json.dump({'remaining': remaining}, f)
    print(f"Log updated, remaining: {remaining}")

def main():
    """Демонстрирует расчёт и обновление статуса очереди в лог-файле.

    Вычисляет оставшееся количество страниц на основе жёстко заданных значений,
    вызывает update_queue_log для записи результата и вывода в консоль.
    """
    total = 100
    processed = 85
    remaining = total - processed
    log_file = "queue_status.json"
    update_queue_log(log_file, remaining)

if __name__ == "__main__":
    main()
