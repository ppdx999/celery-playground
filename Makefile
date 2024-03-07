.PHONY: build
build: ## build main container
	docker compose build

.PHONY: up
up: ## run main container
	docker compose up -d

.PHONY: down
down: ## stop main container
	docker compose down

.PHONY: worker
worker: ## run worker container
	docker compose exec worker bash

.PHONY: server
server: ## run server container
	docker compose exec server bash

.PHONY: ps
ps: ## show container status
	docker compose ps

.PHONY: logs
logs: ## show container logs
	docker compose logs

.PHONY: health
health: ## show container health
	@curl http://localhost:8080 -s -o /dev/null -w "%{http_code}\n"

.PHONY: help
help: ## show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
