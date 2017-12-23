import hug

import endpoints.v1 as v1

router = hug.route.API(__name__)

router.urls()

# TODO: change naming of id to uuid

# display welcome message
router.get('/', versions=1, examples='')(v1.welcome)

# get all lists, paginated
router.get('/lists/', versions=1, examples='page_index=0&page_size=3')(v1.get_lists_page)

# create a new list
router.post('/lists/', versions=1, examples='')(v1.create_list)

# delete a list by id
router.delete('/lists/{list_id}/', versions=1, examples='')(v1.delete_list)

# get list info and first page of entries
router.get('/lists/{list_id}/', versions=1, examples='page_size=3')(v1.get_list_meta_and_first_entry_page)

# get list meta-info
router.get('/lists/{list_id}/meta/', versions=1, examples='')(v1.get_list_meta)

# get a page of entries for the specified list
router.get('/lists/{list_id}/entries/', versions=1, examples='page_index=0&page_size=3')(
	v1.get_list_entries_page)

# add an learning entry to a learning list
router.post('/lists/{list_id}/entries/', versions=1, examples='')(v1.create_list_entry)

# remove an learning entry from a learning list
router.delete('/lists/{list_id}/entries/{entry_id}', versions=1, examples='')(v1.delete_list_entry)
