TAG = latest

build-image:
	docker build -t nameko/gateway_2:$(TAG) ./gateway

docker-tag:
	docker tag nameko/gateway_2:$(TAG) \
	nameko/gateway_2:$(TAG)

push-image:
	docker push nameko/gateway_2:$(TAG)
