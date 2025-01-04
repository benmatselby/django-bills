MYSQL_VERSION ?= 9.1.0
BILLS_DATABASE_USER ?= root
BILLS_DATABASE_PASSWORD ?= password
BILLS_DATABASE_HOST ?= 127.0.0.1
BILLS_DATABASE_NAME ?= house


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
	docker run -d -p 3306:3306 -eMYSQL_ROOT_PASSWORD=${BILLS_DATABASE_PASSWORD} --name mysql mysql:${BILLS_DATABASE_PASSWORD}
	sleep 10
	docker exec -it mysql mysql -h 127.0.0.1 -uroot -p${BILLS_DATABASE_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS house;"

.PHONY: run
run: ## Run the application
	BILLS_DATABASE_USER=${BILLS_DATABASE_USER} \
	BILLS_DATABASE_PASSWORD=${BILLS_DATABASE_PASSWORD} \
	BILLS_DATABASE_HOST=${BILLS_DATABASE_HOST} \
	BILLS_DATABASE_NAME=${BILLS_DATABASE_NAME} \
	uv run python manage.py runserver 0.0.0.0:8000

.PHONY: lint
lint: ## Lint the application
	uv run ruff check

.PHONY: test
test: ## Test the application
	uv run manage.py test
