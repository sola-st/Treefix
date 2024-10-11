# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
unicode_dict = {unicode_key: "value1"}
assert unicode_dict == ujson.decode(ujson.encode(unicode_dict))
