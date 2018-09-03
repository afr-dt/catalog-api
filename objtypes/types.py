import graphene
from graphene import relay
from graphene.relay import Connection, ConnectionField
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models.models import (
    Item as ItemModel,
    Area as AreaModel,
    Catalog as CatalogModel
)


class Item(SQLAlchemyObjectType):
    """Item Object"""
    class Meta:
        model = ItemModel
        interfaces = (relay.Node, )


class Area(SQLAlchemyObjectType):
    """Area Object"""
    class Meta:
        model = AreaModel
        interfaces = (relay.Node, )


class Catalog(SQLAlchemyObjectType):
    """Catalog Object"""
    class Meta:
        model = CatalogModel
        interfaces = (relay.Node, )
