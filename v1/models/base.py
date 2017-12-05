import datetime
import uuid as uuid

from peewee import *
from playhouse.shortcuts import model_to_dict

# defining our database
db = PostgresqlDatabase('kannji', user='root', password='qwer1234', host='kannji-db')


class BaseModel(Model):
	uuid = UUIDField(primary_key=True, default=uuid.uuid4)
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)
	
	# override the save method to update 'updated_at' on every change
	def save(self, *args, **kwargs):
		self.updated_at = datetime.datetime.now()
		return super(BaseModel, self).save(*args, **kwargs)
	
	# override the to_dict method to have to be able to care about the uuid
	# the uuid must be converted to a string manually, otherwise it cannot be JSON encoded
	# the JSON encoder will throw an TypeError
	def to_dict(self):
		# convert model to dictionary
		dict = model_to_dict(self)
		# because JSON does not like to encode a uuid, we need to prepare our dictionary accordingly
		# TODO have a prettier solution for that
		dict['uuid'] = str(dict['uuid'])
		return dict
	
	class Meta:
		database = db
