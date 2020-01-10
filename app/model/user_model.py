from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, StringField, IntField
)
import hashlib

class User(Document):
    mongooseVersion = IntField(db_field="__v")
    meta = {'collection': 'users'}
    id = StringField(db_field="_id")
    email = StringField()
    password = StringField()
    created_at = DateTimeField(db_field="createdAt", default=datetime.now)

    def verify_password(self, password):
        m = hashlib.sha256()
        m.update(password.encode('utf-8'))
        return self.password == m.hexdigest()