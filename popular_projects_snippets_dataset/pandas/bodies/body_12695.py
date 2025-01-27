# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(builtin_value)
assert builtin_value == json.loads(output)
assert output == json.dumps(builtin_value)
assert builtin_value == ujson.decode(output)
