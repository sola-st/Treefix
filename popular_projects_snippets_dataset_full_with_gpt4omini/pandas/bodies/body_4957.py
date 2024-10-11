# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#32432
df = DataFrame({"A": [True, False], "B": [1, 2]})
result = df.any(axis=1, bool_only=True)
expected = Series([True, False])
tm.assert_series_equal(result, expected)
