# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(num_input)
assert num_input == json.loads(output)
assert output == json.dumps(num_input)
assert num_input == ujson.decode(output)
