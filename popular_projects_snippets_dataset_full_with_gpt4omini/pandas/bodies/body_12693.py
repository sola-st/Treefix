# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
list_input = [1, 2, 3, 4]
output = ujson.encode(list_input)

assert list_input == json.loads(output)
assert list_input == ujson.decode(output)
