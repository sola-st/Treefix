# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#48778

df = DataFrame({"a": [1, pd.NA, pd.NA], "b": pd.NA}, dtype=any_numeric_ea_dtype)
# Warning from numpy for taking std of single element
with tm.assert_produces_warning(RuntimeWarning, check_stacklevel=False):
    result = df.describe()
expected = DataFrame(
    {"a": [1.0, 1.0, pd.NA] + [1.0] * 5, "b": [0.0] + [pd.NA] * 7},
    index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"],
    dtype="Float64",
)
tm.assert_frame_equal(result, expected)
