TAG = latest

build-image:
	docker build -t nameko/travel_agent_2:$(TAG) ./travel_agent_2

docker-tag:
	docker tag nameko/travel_agent_2:$(TAG) \
	nameko/travel_agent_2:$(TAG)

push-image:
	docker push nameko/travel_agent_2:$(TAG)
