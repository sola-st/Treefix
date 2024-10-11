# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# GH#13067
idx = PeriodIndex([], freq="M")
result = idx._view()
expected = idx

tm.assert_index_equal(result, expected)
