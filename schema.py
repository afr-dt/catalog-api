import graphene
from sqlalchemy import update
from graphene import relay, Connection
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from mutations.mutations import CreateItem
from objtypes.types import (Item, ItemModel)


class Query(graphene.ObjectType):

    items = SQLAlchemyConnectionField(
        Item, status=graphene.Boolean(), required=False)

    item = graphene.Field(lambda: Item, item_id=graphene.Int())

    def resolve_item(self, info, item_id):
        query = Item.get_query(info)
        return query.filter(ItemModel.item_id == item_id).first()


class ServicesMutations(graphene.ObjectType):
    create_item = CreateItem.Field()


schema = graphene.Schema(query=Query, mutation=ServicesMutations, types=[
                         Item], auto_camelcase=False)
