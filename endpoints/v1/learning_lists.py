import hug

from models import LearningEntry
from models import LearningList


def get_lists_page(page_index: hug.types.greater_than(-1), page_size: hug.types.greater_than(0)):
	learning_lists_meta_page_query = LearningList.select().order_by(LearningList.created_at).paginate(page_index + 1,
	                                                                                                  page_size)
	# iterate over all learning list to trigger their loading (they are lazy-loaded)
	# and convert them to dictionaries
	learning_lists_page = [current_learning_list.to_dict() for current_learning_list in learning_lists_meta_page_query]
	return learning_lists_page


def get_list_meta_and_first_entry_page(list_id: hug.types.uuid, page_size: hug.types.greater_than(0)):
	learning_list_query = LearningList.get(LearningList.uuid == list_id)
	learning_list = learning_list_query.to_dict()
	# iterate over all learning entries for this list to trigger their loading (they are lazy-loaded)
	# and convert them to dictionaries
	learning_list['entries'] = [current_learning_entry.to_dict() for current_learning_entry in
	                            learning_list_query.learning_entries]
	return learning_list


def get_list_meta(list_id: hug.types.uuid):
	learning_list_meta_query = LearningList.get(LearningList.uuid == list_id)
	return learning_list_meta_query.to_dict()


def create_list(body: hug.types.json):
	new_list = LearningList(name=body['name'], description=body['description'])
	# as wer are not using a integer id, but a string containing a uuid, auto-increment on db side does not work,
	# thus we need to explicitly state that we want to insert.
	new_list.save(force_insert=True)
	return new_list.to_dict()


def get_list_entries_page(list_id: hug.types.uuid, page_index: hug.types.greater_than(-1),
                          page_size: hug.types.greater_than(0)):
	learning_list_entries_page_query = LearningEntry.select().join(LearningList).where(
		LearningList.uuid == list_id).order_by(LearningList.created_at).paginate(page_index + 1,
	                                                                             page_size)
	# iterate over all learning entries for the requested list to trigger their loading (they are lazy-loaded)
	# and convert them to dictionaries
	learning_list_entries_page = [current_learning_entry.to_dict() for current_learning_entry in
	                              learning_list_entries_page_query]
	return learning_list_entries_page


def create_list_entry(list_id: hug.types.uuid, body: hug.types.json):
	new_list_entry = LearningEntry(learning_list=list_id, kanji_writing=body['kanji_writing'],
	                               kana_writing=body['kana_writing'], translation=body['translation'])
	# as wer are not using a integer id, but a string containing a uuid, auto-increment on db side does not work,
	# thus we need to explicitly state that we want to insert.
	new_list_entry.save(force_insert=True)
	return new_list_entry.to_dict()
