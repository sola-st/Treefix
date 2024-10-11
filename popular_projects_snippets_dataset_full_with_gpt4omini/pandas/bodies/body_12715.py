# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
long_input = [
    9223372036854775807,
    9223372036854775807,
    9223372036854775807,
    9223372036854775807,
    9223372036854775807,
    9223372036854775807,
]
output = ujson.encode(long_input)

assert long_input == json.loads(output)
assert long_input == ujson.decode(output)
