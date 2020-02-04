import json
json_data = '{"a": 1, "e": 2, "c": 3, "d": 4, "b":5}'

parsed_json = (json.loads(json_data))
print(json.dumps(parsed_json, indent=4, sort_keys=True))