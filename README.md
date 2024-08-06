# Игра Жизни (Game of Life)

Этот проект представляет собой реализацию клеточного автомата "Игра Жизни" Джона Конвея с использованием PyQt6 для графического интерфейса и NumPy для работы с сеткой.

## Описание

Игра Жизни — это клеточный автомат, состоящий из сетки клеток, каждая из которых может быть живой или мёртвой. Клетки развиваются в соответствии с набором правил, учитывающих состояние соседних клеток.

Приложение позволяет:
- Запускать и останавливать симуляцию.
- Сбрасывать сетку в исходное состояние.
- Настраивать скорость симуляции.
- Размещать предопределённые шаблоны (паттерны) на сетке.

## Установка и запуск

1. **Клонируйте репозиторий:**

    ```sh
    git clone https://github.com/rubila341/game_of_life.git
    cd game_of_life
    ```

2. **Создайте виртуальную среду:**

    ```sh
    python -m venv .venv
    ```

3. **Активируйте виртуальную среду:**

    - На Windows:

      ```sh
      .venv\Scripts\activate
      ```

    - На macOS/Linux:

      ```sh
      source .venv/bin/activate
      ```

4. **Установите зависимости:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Запустите приложение:**

    ```sh
    python main.py
    ```

## Использование

- **Запуск/Остановка симуляции:** Используйте кнопки 'Start' и 'Stop' для управления симуляцией.
- **Сброс сетки:** Используйте кнопку 'Reset' для очистки сетки.
- **Настройка скорости:** Используйте ползунок для установки скорости симуляции.
- **Выбор шаблона:** Нажмите на один из предопределённых шаблонов, чтобы разместить его на сетке.

## Файлы

- **`main.py`**: Основной скрипт для запуска приложения.
- **`game_of_life_ui.py`**: Содержит класс `Canvas` для отрисовки сетки и обработки событий мыши.
- **`game_of_life_utils.py`**: Вспомогательные функции и классы для логики игры и работы с сеткой.
- **`requirements.txt`**: Список необходимых Python-библиотек.