# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(long_input)

assert long_input == json.loads(output)
assert output == json.dumps(long_input)
assert long_input == ujson.decode(output)
