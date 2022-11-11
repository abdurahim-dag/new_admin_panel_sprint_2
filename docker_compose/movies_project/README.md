docker-compose  --env-file ./.env.dev up -d --no-deps --build
docker compose -f docker-compose.yml -f docker-compose.prod.yml --env-file ./.env.prod up -d

docker exec -it app-movie python manage.py migrate
docker exec -it app-movie python manage.py collectstatic --no-input
docker exec -it app-movie python manage.py createsuperuser
docker exec -it app-movie bash -c "cd /app; python -m sqlite_to_postgres.load_data"