from fastapi import FastAPI, HTTPException, Body
from typing import List
from pydantic import BaseModel, Field

app = FastAPI(
    title="OpenAPI Жақсартылған Құжаттама",
    description="Бұл API мысалы OpenAPI мүмкіндіктерін толық қолданады",
    version="1.0.0"
)

items_db = []

class Item(BaseModel):
    name: str = Field(..., description="Заттың атауы", example="Ноутбук")
    price: float = Field(..., description="Заттың бағасы", example=249999.99)

@app.get("/ping", tags=["Сервис"], summary="Пинг", description="Сервердің тірі екенін тексереді")
async def ping():
    return {"message": "pong"}

@app.post("/items/", response_model=Item, status_code=201,
          tags=["Заттар"], summary="Жаңа зат қосу",
          description="Жаңа затты жүйеге қосады",
          responses={201: {"description": "Сәтті қосылды"}, 400: {"description": "Қате енгізу"}})
async def create_item(
    item: Item = Body(
        ...,
        examples={
            "notebook": {
                "summary": "Ноутбук мысалы",
                "description": "Қарапайым ноутбук",
                "value": {"name": "Ноутбук", "price": 399990}
            },
            "phone": {
                "summary": "Смартфон мысалы",
                "description": "Орта сегменттегі телефон",
                "value": {"name": "Samsung A52", "price": 199990}
            }
        }
    )
):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Баға 0-ден жоғары болуы керек")
    items_db.append(item)
    return item

@app.get("/items/", response_model=List[Item],
         tags=["Заттар"],
         summary="Барлық заттарды көру",
         description="Барлық тіркелген заттарды қайтарады.")
async def get_items():
    return items_db

@app.get("/", tags=["Сервис"], summary="API-дің басты беті")
async def root():
    return {"message": "Бұл API тауарлармен жұмыс істеуге арналған"}
