# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
recs = [{"flat1": 1, "flat2": 2}, {"flat3": 3, "flat2": 4}]
result = nested_to_record(recs)
expected = recs
assert result == expected
