from connect import bd
from mongoengine import *


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField("Authors")
    quote = StringField()


class Users(Document):
    fullname = StringField()
    email_address = StringField()
    take_msg = BooleanField(default=False)
