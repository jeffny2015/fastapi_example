from fastapi import FastAPI
from api import query, cat

# more info about documentation https://fastapi.tiangolo.com/tutorial/metadata/#:~:text=You%20can%20disable%20it%20by%20setting%20docs_url%3DNone%20.
app = FastAPI(
    tittle="SQL API",
    description="Execute queries into SQL",
    version="1.0.0",
    contact={
        "name" : "Jeffrey Alfaro",
        "email" : "jeffny2015@gmail.com"
    },
    license_info = {
        "name": "MIT"
    }
)


app.include_router(query.router)
app.include_router(cat.router)