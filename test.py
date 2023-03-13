import unittest
from unittest.mock import patch, mock_open
from main import sniff_schema
import json


class TestSniffSchema(unittest.TestCase):

    def test_sniff_schema(self):
        # Define test data
        data = {
            "name": "John Smith",
            "age": 35,
            "is_student": False,
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA",
                "zip": 12345
            },
            "phone_numbers": [
                {"type": "home", "number": "555-1234"},
                {"type": "work", "number": "555-5678"}
            ],
            "email": "john.smith@example.com"
        }

        # Define expected schema
        expected_schema = {
            "name": {"type": "string", "tag": "", "description": "", "required": False},
            "age": {"type": "integer", "tag": "", "description": "", "required": False},
            "is_student": {"type": "boolean", "tag": "", "description": "", "required": False},
            "address.street": {"type": "string", "tag": "", "description": "", "required": False},
            "address.city": {"type": "string", "tag": "", "description": "", "required": False},
            "address.state": {"type": "string", "tag": "", "description": "", "required": False},
            "address.zip": {"type": "integer", "tag": "", "description": "", "required": False},
            "phone_numbers": {
                "type": "array",
                "tag": "",
                "description": "",
                "required": False,
                "items": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "tag": "", "description": "", "required": False},
                        "number": {"type": "string", "tag": "", "description": "", "required": False}
                    },
                    "required": False
                }
            },
            "email": {"type": "string", "tag": "", "description": "", "required": False}
        }

        # Test sniff_schema function
        with patch('builtins.open', new_callable=mock_open, read_data=json.dumps({'message': data})):
            actual_schema = sniff_schema(data)

        # Debugging output
        print(f"actual_schema: {actual_schema}")
        print(f"expected_schema: {expected_schema}")

        # Assert actual vs. expected schema
        self.maxDiff = None
        self.assertDictEqual(actual_schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
