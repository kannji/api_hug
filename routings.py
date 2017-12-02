import hug

from v1 import learning_lists, index

router = hug.route.API(__name__)

router.urls()

# display welcome message
router.get('/', versions=1, examples='')(index.welcome)

# get all lists, paginated
router.get('/lists/', versions=1, examples='page_index=0&page_size=3')(learning_lists.get_lists_page)

# get list info and first page of entries
router.get('/lists/{list_id}/', versions=1, examples='page_size=3')(learning_lists.get_list_meta_and_first_entry_page)

# get list meta-info
router.get('/lists/{list_id}/meta/', versions=1, examples='')(learning_lists.get_list_meta)

# get a page of entries for the specified list
router.get('/lists/{list_id}/entries/', versions=1, examples='page_index=0&page_size=3')(
	learning_lists.get_list_entries_page)
