# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
doubles_input = [31337.31337, 31337.31337, 31337.31337, 31337.31337] * 10
output = ujson.encode(doubles_input)

assert doubles_input == json.loads(output)
assert doubles_input == ujson.decode(output)
