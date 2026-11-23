import os, redis
import random, string
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

app = FastAPI()
Instrumentator().instrument(app).expose(app)
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/health")
def health_check():
    return {"status": "ok"}

class URLItem(BaseModel):
    url: str

def generate_short_id(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=length))

@app.post("/shorten")
def shorten_url(item: URLItem):
    short_id = generate_short_id()
    r.set(short_id, item.url)
    return {"short_id": short_id, "original_url": item.url}

@app.get("/{short_id}")
def redirect_to_url(short_id: str):
    original_url = r.get(short_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)
