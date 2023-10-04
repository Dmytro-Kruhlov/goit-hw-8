from connect import uri
from mongoengine import *

db = connect(host=uri, ssl=True, db="hw8")


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField("Authors")
    quote = StringField()
