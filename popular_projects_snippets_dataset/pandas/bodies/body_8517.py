# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
rng = date_range("1/1/2000", "1/1/2010")

result = rng.get_loc("2009")
expected = slice(3288, 3653)
assert result == expected
