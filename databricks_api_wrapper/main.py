from fastapi import FastAPI
import uvicorn

from .routes import clusters


app = FastAPI()

app.include_router(clusters.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("databricks_api_wrapper.main:app",
                host="0.0.0.0", port=8000, reload=True)
