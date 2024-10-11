# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
assert ujson.decode(int_exp) == json.loads(int_exp)
