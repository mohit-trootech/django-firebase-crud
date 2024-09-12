from django.db.models import *
from django_extensions.db.models import (
    TitleDescriptionModel,
    TimeStampedModel,
    ActivatorModel,
)


class Employee(TitleDescriptionModel, TimeStampedModel, ActivatorModel):

    age = IntegerField()
    position = CharField()
    city = CharField()
    salary = DecimalField()

    def __str__(self) -> str:
        return self.title
