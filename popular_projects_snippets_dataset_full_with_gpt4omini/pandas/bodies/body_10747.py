# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH-34047
df = DataFrame({"a": Series([1, None, 2], dtype=dtype)})
orig = df.copy()
gb = df.groupby(groups)["a"]

result = getattr(gb, method)(skipna=False)
expected = Series(expected_data, dtype=dtype, name="a")

# check we didn't accidentally alter df
tm.assert_frame_equal(df, orig)

tm.assert_series_equal(result, expected)
