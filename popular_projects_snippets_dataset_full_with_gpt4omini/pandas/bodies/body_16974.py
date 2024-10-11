# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH#39817, GH#45101
result = concat([Series(dtype=left), Series(dtype=right)])
assert result.dtype == expected
