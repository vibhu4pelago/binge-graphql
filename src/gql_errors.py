import graphene
from graphene.types.generic import GenericScalar


class BingeError(graphene.ObjectType):
    error_header = graphene.String()
    error_message = graphene.String()
    code = graphene.Int()
    error_details = GenericScalar()


class BingeListError(graphene.ObjectType):

    error_message = graphene.String()
    code = graphene.Int()
