import json
import unittest

import hug

from hug_extensions.types.json_structure import JSONStructure


class TestJSONStructure(unittest.TestCase):
	
	def test_empty_json(self):
		structure = {}
		json_str = "{}"
		result = {}
		self.assertEqual(JSONStructure(structure)(json_str), result)
	
	def test_one_key_json(self):
		structure = {
			'name': hug.types.text
		}
		result = {
			'name': 'Jan-Luca Klees'
		}
		self.assertEqual(JSONStructure(structure)(json.dumps(result)), result)
	
	def test_multiple_keys_json(self):
		structure = {
			'name': hug.types.text,
			'age': hug.types.number
		}
		result = {
			'name': 'Jan-Luca Klees',
			'age': 23
		}
		self.assertEqual(JSONStructure(structure)(json.dumps(result)), result)
	
	def test_nested_json(self):
		structure = {
			'name': {
				'first': hug.types.text,
				'last': hug.types.text,
			}
		}
		result = {
			'name': {
				'first': 'Jan-Luca',
				'last': 'Klees',
			}
		}
		self.assertEqual(JSONStructure(structure)(json.dumps(result)), result)
	
	def test_deeply_nested_json(self):
		structure = {
			'some': {
				'deeply': {
					'nested': {
						'key': hug.types.text
					}
				}
			}
		}
		result = {
			'some': {
				'deeply': {
					'nested': {
						'key': 'value'
					}
				}
			}
		}
		self.assertEqual(JSONStructure(structure)(json.dumps(result)), result)


if __name__ == '__main__':
	unittest.main()
