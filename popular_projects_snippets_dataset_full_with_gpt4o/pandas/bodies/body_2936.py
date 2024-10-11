# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dtypes.py
# GH46409
df = DataFrame(
    {"id": [1, 2, 3, 4], "test": [True, pd.NA, data, False]}
).convert_dtypes()
result = df.groupby("id").last().test
expected = df.set_index("id").test
assert result.dtype == pd.BooleanDtype()
tm.assert_series_equal(expected, result)
