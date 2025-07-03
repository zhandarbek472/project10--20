from fastapi import FastAPI, HTTPException
from redis_cache import get_cache, set_cache, delete_cache

app = FastAPI()

# Условная база данных (in-memory)
notes_db = [
    {"id": 1, "text": "First note"},
    {"id": 2, "text": "Second note"}
]


@app.get("/notes")
async def get_notes():
    cache_key = "notes_all"
    cached = await get_cache(cache_key)
    if cached:
        return {"source": "cache", "data": cached}

    # Имитируем задержку (настоящий запрос к БД)
    data = notes_db
    await set_cache(cache_key, data, expire_seconds=60)
    return {"source": "db", "data": data}


@app.post("/notes")
async def add_note(note: dict):
    notes_db.append(note)
    await delete_cache("notes_all")
    return {"message": "Note added"}


@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    global notes_db
    notes_db = [n for n in notes_db if n["id"] != note_id]
    await delete_cache("notes_all")
    return {"message": "Note deleted"}
