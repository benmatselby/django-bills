MYSQL_VERSION ?= 8.1.0
MYSQL_PASSWORD ?= password

.PHONY: install
install: ## Install the dependencies
	pipenv install

.PHONY: bootstrap
bootstrap: ## Bootstrap the application
	pipenv run python manage.py migrate
	pipenv run python manage.py makemigrations
	# pipenv run python manage.py createsuperuser

.PHONY: run
run: ## Run the application
	docker run -d -p 3306:3306 -eMYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} --name mysql mysql:${MYSQL_VERSION}
	sleep 10
	docker exec -it mysql mysql -h 127.0.0.1 -uroot -p${MYSQL_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS house;"
	pipenv run python manage.py runserver
