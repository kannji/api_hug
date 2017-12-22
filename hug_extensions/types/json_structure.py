import hug


class JSONStructure(hug.types.JSON):
	__slots__ = ('structure',)
	
	def __init__(self, structure):
		super().__init__()
		self.structure = structure
	
	def _validate_json_against_structure(self, structure, json):
		for key in structure:
			current_structure = structure[key]
			
			# check if key exists in JSON
			if key in json:
				current_json = json[key]
			else:
				raise ValueError('Provided json is missing key: {0}'.format(key))
			
			# key does exists in json, check if iit si a dict and if we ned to recurse
			if type(current_structure) is dict:
				json[key] = self._validate_json_against_structure(current_structure, current_json)
			else:
				json[key] = current_structure(current_json)
		
		return json
	
	def __call__(self, value):
		json = super().__call__(value)
		
		return self._validate_json_against_structure(self.structure, json)
