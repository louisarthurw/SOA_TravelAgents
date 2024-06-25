TAG = latest

build-image:
	docker build -t nameko/travel_agent_1:$(TAG) ./travel_agent_1

docker-tag:
	docker tag nameko/travel_agent_1:$(TAG) \
	nameko/travel_agent_1:$(TAG)

push-image:
	docker push nameko/travel_agent_1:$(TAG)
