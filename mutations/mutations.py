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


class AreaInput(graphene.InputObjectType):
    """Area Input"""
    area_id = graphene.Int(required=False)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    created = graphene.String(required=False)
    updated = graphene.String(required=False)


class CreateArea(graphene.Mutation):
    """Create Area"""
    class Arguments:
        area_data = AreaInput(required=True)
    area = graphene.Field(Area)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, area_data=None):
        try:
            area = AreaModel(**area_data)
            db_session.add(area)
            db_session.commit()
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error inserting Area... {}".format(err))


class CatalogInput(graphene.InputObjectType):
    """Catalog Input"""
    catalog_id = graphene.Int(required=False)
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    created = graphene.String(required=False)
    updated = graphene.String(required=False)


class CreateCatalog(graphene.Mutation):
    """Create Catalog"""
    class Arguments:
        catalog_data = CatalogInput(required=True)
    catalog = graphene.Field(Catalog)
    status = graphene.Boolean()

    @staticmethod
    def mutate(root, info, catalog_data=None):
        try:
            catalog = CatalogModel(**catalog_data)
            db_session.add(catalog)
            db_session.commit()
        except BaseException as err:
            db_session.rollback()
            raise GraphQLError("Error inserting Catalog... {}".format(err))
