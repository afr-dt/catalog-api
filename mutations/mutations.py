import graphene
from config import db_session
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError
from sqlalchemy import update

from objtypes.types import (
    Item, ItemModel,
    Area, AreaModel,
    Catalog, CatalogModel
)


class ItemInput(graphene.InputObjectType):
    """Item Input"""
    item_id = graphene.Int(required=False)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    created = graphene.String(required=False)
    updated = graphene.String(required=False)


class CreateItem(graphene.Mutation):
    """Create Item"""
    class Arguments:
        item_data = ItemInput(required=True)
    item = graphene.Field(Item)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, item_data=None):
        try:
            item = ItemModel(**item_data)
            db_session.add(item)
            db_session.commit()
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error inserting Item... {}".format(err))
