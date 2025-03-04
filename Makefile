install:
	uv sync


brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/hexlet_code-0.1.0-py3-none-any.whl

make lint:
	uv run ruff check brain_games --fix
brain-even:
	uv run brain-even
brain-calc:
	uv	run	brain-calc
brain-gcd:
	uv	run	brain-gcd
brain-prime:
	uv	run	brain-prime

brain-progression:
	uv run brain-progression


