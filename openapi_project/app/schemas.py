from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="Атауы", example="Ноутбук")
    price: float = Field(..., description="Бағасы", example=399990.00)
    quantity: int = Field(..., description="Саны", example=2)
