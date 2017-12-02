import hug


def get_lists_page(page_index: hug.types.greater_than(-1), page_size: hug.types.greater_than(0)):
	return {
		'page_count': 1,
		'learning_lists': [
			{
				'uuid': '3154ab38-4167-4a04-9615-902ae7249dbd',
				'name': 'All JLPT Kanji!',
				'description': 'leanr all JlPT kanji with this list and master japanese kanji!',
				'thumbnail_url': 'https://research.owlfolio.org/scratchpad/resolver.jpeg'
			},
			{
				'uuid': '3154ab38-4167-4a04-9615-902ae7249dbd',
				'name': 'Minna no Nihongo',
				'description': 'All minna no nihongo vocabulary for minna no nihongo 1.',
				'thumbnail_url': 'https://research.owlfolio.org/scratchpad/resolver.jpeg'
			},
			{
				'uuid': '3154ab38-4167-4a04-9615-902ae7249dbd',
				'name': 'Tomodachi Vol. 2',
				'description': 'The vocabulary from the tomodachi Vol.2 book.',
				'thumbnail_url': 'https://research.owlfolio.org/scratchpad/resolver.jpeg'
			}
		]
	}


def get_list_meta_and_first_entry_page(list_id: hug.types.uuid, page_size: hug.types.greater_than(0)):
	return {
		'info': get_list_meta(list_id),
		'entries': get_list_entries_page(list_id=list_id, page_index=0, page_size=page_size)
	}


def get_list_meta(list_id: hug.types.uuid):
	return {
		'uuid': str(list_id),
		'name': 'All JLPT Kanji!',
		'description': 'leanr all JlPT kanji with this list and master japanese kanji!',
		'thumbnail_url': 'https://research.owlfolio.org/scratchpad/resolver.jpeg'
	}


def get_list_entries_page(list_id: hug.types.uuid, page_index: hug.types.greater_than(-1),
                          page_size: hug.types.greater_than(0)):
	return {
		'page_count': 1,
		'entries': [
			{
				'uuid': '3154ab38-4167-4a04-9615-902ae7249dbd',
				'kanji': '大学',
				'reading': 'だいがく',
				'translation': 'university'
			}
		]
	}
