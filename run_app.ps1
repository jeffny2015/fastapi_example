cd postgres
docker compose up --force-recreate --build -d
cd ..

uvicorn --app-dir=./src app:app --reload