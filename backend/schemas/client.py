from pydantic import BaseModel, EmailStr
from typing import List, Optional

class DealBase(BaseModel):
    id: int
    title: str
    amount: float

    class Config:
        orm_mode = True

class FinanceBase(BaseModel):
    type: int
    amount: float
    description: str

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    name: str
    number_phone: int
    email: EmailStr

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    number_phone: Optional[str] = None
    email: Optional[EmailStr] = None

class ClientInDBBase(ClientBase):
    id: int
    deals: List[DealBase] = []
    finances: List[FinanceBase] = []

    class Config:
        orm_mode = True

class ClientDB(ClientInDBBase):
    pass

