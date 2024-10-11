# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 46719
df = DataFrame(
    {"col1": [3, "string", float], "col2": [0.25, datetime(2020, 1, 1), np.nan]},
    index=["a", "b", "c"],
)

# applymap
result = df.applymap(type)
expected = DataFrame(
    {"col1": [int, str, type], "col2": [float, datetime, float]},
    index=["a", "b", "c"],
)
tm.assert_frame_equal(result, expected)

# axis=0
result = df.apply(type, axis=0)
expected = Series({"col1": Series, "col2": Series})
tm.assert_series_equal(result, expected)

# axis=1
result = df.apply(type, axis=1)
expected = Series({"a": Series, "b": Series, "c": Series})
tm.assert_series_equal(result, expected)
