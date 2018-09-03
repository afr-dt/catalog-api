import graphene
from sqlalchemy import update
from graphene import relay, Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from mutations.mutations import CreateItem, CreateArea, CreateCatalog
from objtypes.types import (Item, ItemModel, Area,
                            AreaModel, Catalog, CatalogModel)


class Query(graphene.ObjectType):

    items = SQLAlchemyConnectionField(
        Item, status=graphene.Boolean(), required=False)
    item = graphene.Field(lambda: Item, item_id=graphene.Int())

    def resolve_item(self, info, item_id):
        query = Item.get_query(info)
        return query.filter(ItemModel.item_id == item_id).first()

    areas = SQLAlchemyConnectionField(
        Area, status=graphene.Boolean(), required=False)
    area = graphene.Field(lambda: Area, area_id=graphene.Int())

    def resolve_area(self, info, area_id):
        query = Area.get_query(info)
        return query.filter(AreaModel.area_id == area_id).first()

    catalogs = SQLAlchemyConnectionField(
        Catalog, status=graphene.Boolean(), required=False)
    catalog = graphene.Field(lambda: Catalog, catalog_id=graphene.Int())

    def resolve_catalog(self, info, catalog_id):
        query = Catalog.get_query(info)
        return query.filter(CatalogModel.catalog_id == catalog_id).first()


class ServicesMutations(graphene.ObjectType):
    create_item = CreateItem.Field()
    create_area = CreateArea.Field()
    create_catalog = CreateCatalog.Field()


schema = graphene.Schema(query=Query, mutation=ServicesMutations, types=[
                         Item], auto_camelcase=False)
