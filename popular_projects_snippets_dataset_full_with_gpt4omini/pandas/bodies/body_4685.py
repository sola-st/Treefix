# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# GH8383
result = numpy_op(Series([1, 2, 3, 4]))
assert result == expected
