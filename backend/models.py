from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Float, Boolean, Text
from sqlalchemy.orm import relationship

from backend.database import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    number_phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    deals = relationship('DealBase', back_populates='client') # связь с таблицей Dealbase, одинклиент имее много сделок
    finance =relationship('FinanceBase', back_populates='client')


class Deal(Base):
    __tablename__ = 'deals'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False,index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum, nullable=False)
    clients = relationship('ClientBase', back_populates='deals')
    finance = relationship('FinanceBase', back_populates='deals')

class Finance(Base):
    __tablename__ = 'finances'
    id = Column(Integer, primary_key=False, index=True)
    type = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    discription = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    clients = relationship('ClientBase', back_populates='finance')
    deals = relationship('DealBase', back_populates='finance')


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    deal_id = Column(Date, ForeignKey('clients.id'), nullable=False)
    deadline = Column(Date, nullable=False)
    completed = Column(Boolean, nullable=False)

