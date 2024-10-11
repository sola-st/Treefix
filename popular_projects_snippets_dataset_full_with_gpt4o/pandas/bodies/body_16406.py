# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_util.py
# empty product (empty input):
result = cartesian_product([])
expected = []
assert result == expected
