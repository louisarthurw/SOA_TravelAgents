HTMLCOV_DIR ?= htmlcov
TAG ?= dev
IMAGES := travel_agent gateway

install-dependencies:
	pip install -U -e "travel_agent_3/.[dev]"
	pip install -U -e "gateway/.[dev]"

# docker

build-base:
	docker build --target base -t nameko-example-base . && \
	docker build --target builder -t nameko-example-builder .

build: build-base
	for image in $(IMAGES); do \
		TAG=$(TAG) make -C $$image build-image; \
	done

docker-save:
	mkdir -p docker-images
	docker save -o docker-images/examples.tar $(foreach image,$(IMAGES),nameko/$(image)_3:$(TAG))

docker-load:
	docker load -i docker-images/examples.tar

docker-tag:
	for image in $(IMAGES); do \
		make -C $$image docker-tag; \
	done

docker-login:
	docker login --password=$(DOCKER_PASSWORD) --username=$(DOCKER_USERNAME)

push-images: docker-login
	for image in $(IMAGES); do \
		make -C $$image push-image; \
	done