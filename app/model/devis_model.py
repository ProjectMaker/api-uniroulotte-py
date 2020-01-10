from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, StringField, IntField, DictField
)

class Devis(Document):
    mongooseVersion = IntField(db_field="__v")
    meta = {'collection': 'devis'}
    id = StringField(db_field="_id")
    email = StringField(required=True)
    phone_number = StringField(db_field="phoneNumber")
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    price = StringField(required=True)
    detail = DictField(required=True)
    created_at = DateTimeField(db_field="createdAt", default=datetime.now)