# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
nested_input = [[[[]]]] * 20
output = ujson.encode(nested_input)

assert nested_input == json.loads(output)
assert nested_input == ujson.decode(output)
