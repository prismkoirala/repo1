import graphene
from graphene_django import DjangoObjectType

from .models import Train

class Traintype(DjangoObjectType):
    class Meta:
        model = Train

class Query(graphene.ObjectType):
    train = graphene.List(Traintype)

    def resolve_train(self, info):
        return Train.objects.all()
