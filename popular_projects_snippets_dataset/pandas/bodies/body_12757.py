# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
assert extreme_num == ujson.decode(str(extreme_num))
