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
	uv tool install dist/*.whl