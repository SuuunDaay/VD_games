install:
	uv sync

VD-games:
	uv run VD-games

VD-even:
	uv run VD-even

VD-calc:
	uv run VD-calc

VD-gcd:
	uv run VD-gcd

VD-progression:
	uv run VD-progression

VD-prime:
	uv run VD-prime

build:
	uv build

package-install:
	uv tool install dist/*.whl --force

lint:
	uv run ruff check VD_games
	uv run ruff format --check VD_games

lint-fix:
	uv run ruff check --fix VD_games
	uv run ruff format VD_games

clean:
	rm -rf .venv
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
