# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(double_input)
assert round(double_input, 5) == round(json.loads(output), 5)
assert round(double_input, 5) == round(ujson.decode(output), 5)
