import json
from pathlib import Path
from typing import Union

FilePath = Union[str, Path]

def update_queue_log(file_path, remaining):
    """Обновляет JSON-лог с количеством оставшихся страниц и выводит статус в консоль.

    Args:
        file_path (str): Путь к файлу лога (JSON), может быть строкой или Path.
        remaining (int): Количество оставшихся страниц в очереди.
    """
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump({'remaining': remaining}, f, ensure_ascii=False, indent=4)
    print(f"Лог обновлён. Осталось обработать страниц: {remaining}")


def main() -> None:
    total_pages: int = 100
    processed_pages: int = 85
    remaining_pages: int = total_pages - processed_pages
    log_file_path: Path = Path("queue_status.json")

    should_write_log = False

    if should_write_log:
        update_queue_log(log_file_path, remaining_pages)

    print(f"(main) Осталось обработать страниц: {remaining_pages}")

if __name__ == "__main__":
    main()
