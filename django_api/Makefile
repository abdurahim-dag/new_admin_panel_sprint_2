1-django-migrate:
	docker exec -it app-movie python manage.py migrate
2-django-collstatic:
	docker exec -it app-movie python manage.py collectstatic --no-input
3-django-create-admin:
	docker exec -e DJANGO_SUPERUSER_USERNAME=admin \
                -e DJANGO_SUPERUSER_PASSWORD=1 \
                -e DJANGO_SUPERUSER_EMAIL=mail@mail.ru \
        -it app-movie python manage.py createsuperuser --noinput || true

4-load-sqlite:
	docker exec -it app-movie bash -c "cd /app; python -m sqlite_to_postgres.load_data"

start-dev:
	docker-compose  --env-file ./.env.dev up -d --no-deps --build

0-start-prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml --env-file ./.env.prod up -d

pre-settings: 1-django-migrate 2-django-collstatic 3-django-create-admin 4-load-sqlite
dev-start: start-dev pre-settings
prod-start: 0-start-prod pre-settings