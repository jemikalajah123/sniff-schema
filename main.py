import json


def sniff_schema(data):
    schema = {}
    for key, value in data.items():
        if key == "attributes":
            continue
        if isinstance(value, dict):
            properties = sniff_schema(value)
            for prop_key, prop_value in properties.items():
                schema[key + '.' + prop_key] = prop_value
        elif isinstance(value, list):
            if all(isinstance(item, str) for item in value):
                schema[key] = {
                    "type": "enum",
                    "tag": "",
                    "description": "",
                    "required": False,
                    "enum": value
                }
            elif all(isinstance(item, dict) for item in value):
                items = sniff_schema(value[0])
                schema[key] = {
                    "type": "array",
                    "tag": "",
                    "description": "",
                    "required": False,
                    "items": {
                        "type": "object",
                        "properties": items,
                        "required": False
                    }
                }
        elif isinstance(value, bool):
            schema[key] = {
                "type": "boolean",
                "tag": "",
                "description": "",
                "required": False
            }
        elif isinstance(value, str):
            schema[key] = {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            }
        elif isinstance(value, int):
            schema[key] = {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            }
    return schema


if __name__ == '__main__':
    with open('data/data_2.json') as f:  # change input file here
        data = json.load(f)['message']
        schema = sniff_schema(data)

        with open('schema/schema_2.json', 'w') as outfile:  # change output file here
            json.dump(schema, outfile, indent=4)
