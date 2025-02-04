# Установка зависимостей
install:
	uv sync

# Запуск игры
brain-games:
	uv run brain-games

# Сборка пакета
build:
	uv build

# Установка пакета в систему
package-install:
	uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl
