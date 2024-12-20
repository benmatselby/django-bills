MYSQL_VERSION ?= 9.1.0
MYSQL_PASSWORD ?= password

.PHONY: explain
explain:
	### Welcome
	#
	# .______    __   __       __          _______.
	# |   _  \  |  | |  |     |  |        /       |
	# |  |_   | |  | |  |     |  |       |    ----`
	# |   _  <  |  | |  |     |  |        \   \\
	# |  |_   | |  | |  `----.|  `----.----    |
	# |______/  |__| |_______||_______|_______/
	#
	#
	### Installation
	#
	# $$ make all
	#
	### Targets
	@cat Makefile* | grep -E '^[a-zA-Z_-]+:.*?## .*$$' | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: ## Clean the local folder
	rm -fr .venv
	rm -fr .ruff_cache

.PHONY: install
install: ## Install and run the dependencies
	uv sync
	uv run pre-commit install

.PHONY: bootstrap
bootstrap: ## Bootstrap the application
	uv run python manage.py migrate
	uv run python manage.py createsuperuser
	uv run python manage.py makemigrations

.PHONY: dependencies-run
dependencies-run: ## Run the dependencies
	docker run -d -p 3306:3306 -eMYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} --name mysql mysql:${MYSQL_VERSION}
	sleep 10
	docker exec -it mysql mysql -h 127.0.0.1 -uroot -p${MYSQL_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS house;"

.PHONY: run
run: ## Run the application
	uv run python manage.py runserver

.PHONY: lint
lint: ## Lint the application
	uv run ruff check

.PHONY: test
test: ## Test the application
	uv run manage.py test
