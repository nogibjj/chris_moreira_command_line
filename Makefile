install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=extract --cov=transform --cov=query test_*.py

format:
	black *.py

lint:
	ruff check *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# Deployment instructions go here

all: install lint test format deploy

generate_and_push:
	# Create the markdown log file 
	python test_main.py 

	# Add, commit, and push generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

transform:
	python main.py transform

query_join:
	python main.py query_join

query_aggregate:
	python main.py query_aggregate

query_sort:
	python main.py query_sort

setup_package:
	python setup.py develop --user
