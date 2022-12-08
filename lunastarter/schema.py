import asyncio
import graphene
from graphql import GraphQLError


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
