# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
output = ujson.encode(test)
expected = f'"{test.isoformat()}"'
assert expected == output
