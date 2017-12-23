from peewee import *

from models.base import BaseModel


class SoftDeletable(BaseModel):
	deleted_at = DateTimeField(default=None, null=True)
