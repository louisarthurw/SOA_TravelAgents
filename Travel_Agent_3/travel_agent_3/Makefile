TAG = latest

build-image:
	docker build -t nameko/travel_agent_3:$(TAG) ./travel_agent_3

docker-tag:
	docker tag nameko/travel_agent_3:$(TAG) \
	nameko/travel_agent_3:$(TAG)

push-image:
	docker push nameko/travel_agent_3:$(TAG)
