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

make lint:
	uv run ruff check brain_games
brain-even:
	uv run brain-even
brain-calc:
	uv	run	brain-calc
brain-gcd:
	uv	run	brain-gcd
