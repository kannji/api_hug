from peewee import *

from .base import BaseModel, db


class LearningList(BaseModel):
	name = CharField(max_length=200)
	description = CharField(max_length=2000, null=True)


class LearningEntry(BaseModel):
	learning_list = ForeignKeyField(LearningList, related_name='learning_entries')
	kanji_writing = CharField(max_length=200)
	kana_writing = CharField(max_length=200)
	translation = CharField(max_length=400)
	
	# override the to_dict method to have to be able to care about the uuid
	# the uuid must be converted to a string manually, otherwise it cannot be JSON encoded
	# the JSON encoder will throw an TypeError
	def to_dict(self):
		# convert model to dictionary
		dict = BaseModel.to_dict(self)
		# because JSON does not like to encode a ForeingKeyField, we need to prepare our dictionary accordingly
		# TODO have a prettier solution for that
		del dict['learning_list']
		return dict


# create tables if they don't exist (save=True) in case the database is all new
db.create_tables(models=[LearningList, LearningEntry], safe=True)
