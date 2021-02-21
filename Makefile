-include .env
export

build:
	docker-compose -f docker-compose.yml build

start-local:
	docker-compose -f docker-compose.local.yml up 
	# docker-compose -f docker-compose.local.yml up -d db
	# docker-compose -f docker-compose.local.yml up web

start-prod:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose down --remove-orphans

delete:
	docker-compose down --remove-orphans
	docker-compose -f docker-compose.yml down