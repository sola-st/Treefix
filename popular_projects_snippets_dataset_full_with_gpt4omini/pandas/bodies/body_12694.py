# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
dict_input = {"k1": 1, "k2": 2, "k3": 3, "k4": 4}
output = ujson.encode(dict_input)

assert dict_input == json.loads(output)
assert dict_input == ujson.decode(output)
