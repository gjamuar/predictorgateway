.PHONY: setup lint test run-docker clean

setup:
	bash setup_env.sh

lint:
	poetry run flake8 app

lint-fix:
	poetry run autopep8 --in-place --aggressive --aggressive -r app

test:
	poetry run pytest tests

run-docker:
	docker build -t predictor-gateway . && docker run -d -e PORT=9900 -p 9900:9900 predictor-gateway

clean:
	rm -rf venv

docker-clean:
	docker rmi predictor-gateway || true

logs:
	docker logs -f `docker ps -q -f ancestor=predictor-gateway`