import hug


@hug.get(examples='')
@hug.local()
def info():
    return {'message': 'This is the Kannji api-server running hug.'}
