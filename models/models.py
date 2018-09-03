from sqlalchemy import Table, Column, ForeignKey, DateTime, Time, Date, Integer, String, func, Text
from sqlalchemy.orm import backref, relationship
import datetime

from config import Base
from config import db_session


class Item(Base):
    __tablename__ = 'item'
    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    description = Column(Text)

    area = relationship("Area", uselist=False, back_populates="item")

    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=datetime.datetime.now)


class Area(Base):
    __tablename__ = 'area'
    area_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    description = Column(Text)

    item_id = Column(Integer, ForeignKey('item.item_id'))
    item = relationship("Item", back_populates="area")

    catalog = relationship("Catalog", uselist=False, back_populates="area")

    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=datetime.datetime.now)


class Catalog(Base):
    __tablename__ = 'catalog'
    catalog_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25))
    description = Column(Text)

    area_id = Column(Integer, ForeignKey('area.area_id'))
    area = relationship("Area", back_populates="catalog")

    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=datetime.datetime.now)
