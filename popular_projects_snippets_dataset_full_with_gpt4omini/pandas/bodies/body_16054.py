# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_convert_dtypes.py
# https://github.com/pandas-dev/pandas/issues/31731 -> converting columns
# that are already string dtype
df = pd.DataFrame(
    {"A": ["a", "b", pd.NA], "B": ["ä", "ö", "ü"]}, dtype=nullable_string_dtype
)
result = df.convert_dtypes()
tm.assert_frame_equal(df, result)
