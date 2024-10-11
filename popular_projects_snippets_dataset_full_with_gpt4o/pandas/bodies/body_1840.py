# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
df = DataFrame({"A": 1, "B": 2}, index=date_range("2000", periods=10))
expected = df.copy()

# no warning
g = df.resample("5D", group_keys=False)
with tm.assert_produces_warning(None):
    result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)

# no warning, group keys
expected.index = pd.MultiIndex.from_arrays(
    [pd.to_datetime(["2000-01-01", "2000-01-06"]).repeat(5), expected.index]
)

g = df.resample("5D")
result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)

g = df.resample("5D", group_keys=True)
with tm.assert_produces_warning(None):
    result = g.apply(lambda x: x)
tm.assert_frame_equal(result, expected)
