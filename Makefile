#STACK_FILE:=docker-compose.yml
#
## Spin up local environment
#up: docker-build $(STACK_FILE)
#	@docker-compose -f $(STACK_FILE) up -d


up: docker-build
	docker-compose up -d