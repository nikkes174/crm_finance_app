from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date


class ClientBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

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
    date: date

class FinanceCreate(FinanceBase):
    pass

class FinanceUpdate(FinanceBase):
    type: Optional[int] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    date: Optional[date] = None

class FinanceInDBBase(FinanceBase):
    description: str
    deals: List[DealBase] = []
    finances: List[FinanceBase] = []

class FinanceOut(FinanceBase):
    pass