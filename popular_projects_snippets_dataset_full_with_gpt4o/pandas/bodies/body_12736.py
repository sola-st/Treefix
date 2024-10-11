# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
b = bool(bool_input)
assert ujson.decode(ujson.encode(b)) == b
