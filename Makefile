install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
<<<<<<< HEAD
=======


>>>>>>> 69650e45eb5e85ee6249757f316de0e942921134
