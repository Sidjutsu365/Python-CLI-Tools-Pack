# Python CLI Tools Pack

Набор CLI-утилит на Python для работы с файлами, резервным копированием и логированием.
Проект демонстрирует практическое использование стандартных модулей:
`argparse`, `pathlib`, `shutil`, `subprocess`, `datetime`, `schedule`, `logging`.

---

## Возможности

| Модуль | Назначение | Основные возможности |
|--------|-------------|----------------------|
| **File Organizer** | Сортировка файлов | Распределяет файлы по папкам по типам |
| **Backup Manager** | Резервное копирование | Создаёт копии директорий с интервалом |
| **System Monitor** | Мониторинг системы | Проверяет загрузку CPU, места на диске |

---

## Установка

1. **Клонировать проект**
   
    ```bash
    git clone https://github.com/Sidjutsu365/Python-CLI-Tools-Pack.git
    cd Python-CLI-Tools-Pack

3. **Создать виртуальное окружение**
   
    ```bash
    python3 -m venv venv
    source venv/bin/activate

5. **Установить зависимости**

    ```bash
    pip install -r requirements.txt

---

## Использование CLI

Все утилиты запускаются через общий интерфейс:

    python3 main.py <команда> [агрументы]

### Примеры:

#### File Organizer

    python main.py organizer --source ~/Downloads --target ~/Documents/Sorted
    
#### Backup Scheduler

    python main.py backup --source ~/Downloads --target ~/Download/Backup --interval 5

#### System Monitoring

    python main.py monitor --logfile ~/application.log --interval 2

---

## Основные аргументы

| Модуль | Аргумент | Описание |
|--------|-------------|----------------------|
| **File Organizer** | --source | Путь к исходной папке |
|                    | --target | Путь к целевой папке |
| **Backup Manager** | --source | Путь к исходной папке |
|                    | --target | Путь к целевой папке |
|                    | --interval | Интервал выполнения копирования (мин.) |
| **System Monitor** | --logfile | Пусть к лог-файлу |
|                    | --interval | Интервал выполнения мониторинга (сек.) |

---

## Настройки (config.py)

    FILE_TYPES = {
    "images": (".jpg", ".jpeg", ".png", ".gif"),
    "docs": (".pdf", ".txt", ".docx"),
    "music": (".mp3", ".wav"),
    "archives": (".zip", ".rar", ".tar"),
    }
    
    LOG_PATH = "./logs/main.log"

---

## Пример логгирования

    2025-10-10 10:45:12 - [App] - [INFO] - line 31 - Starting CLI Application...
    2025-10-10 10:45:13 - [App.BackupScheduler] - [INFO] - line 19 - Starting Backup Scheduler App...

---

## Технологии

- Python 3.12+
- argparse — CLI интерфейс
- pathlib — работа с путями
- shutil — файловые операции
- schedule — запуск по расписанию
- subprocess — системные команды
- logging — логирование событий
