docker-compose --env-file ./.env.prod up -d --no-deps --build
docker-compose -f .\docker-compose-dev.yml --env-file ./.env.dev up -d --no-deps --build

docker exec -it app-movie python manage.py collectstatic --no-input
docker exec -it app-movie python manage.py createsuperuser
docker exec -it app-movie bash -c "cd /app; python -m sqlite_to_postgres.load_data"