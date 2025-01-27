# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
assert int(numeric_int_as_str) == ujson.decode(numeric_int_as_str)
