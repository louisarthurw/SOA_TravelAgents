TAG = latest

build-image:
	docker build -t nameko/gateway_3:$(TAG) ./gateway

docker-tag:
	docker tag nameko/gateway_3:$(TAG) \
	nameko/gateway_3:$(TAG)

push-image:
	docker push nameko/gateway_3:$(TAG)
