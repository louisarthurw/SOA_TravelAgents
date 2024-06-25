TAG = latest

build-image:
	docker build -t nameko/gateway_1:$(TAG) ./gateway

docker-tag:
	docker tag nameko/gateway_1:$(TAG) \
	nameko/gateway_1:$(TAG)

push-image:
	docker push nameko/gateway_1:$(TAG)
