# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_append_common.py
# https://github.com/pandas-dev/pandas/issues/19096
a = Series(Categorical(["a", "b", "c"], categories=["a", "b", "c"]))
b = Series(Categorical(["a", "b", "c"], categories=["b", "a", "c"]))
result = pd.concat([a, b], ignore_index=True)
expected = Series(
    Categorical(["a", "b", "c", "a", "b", "c"], categories=["a", "b", "c"])
)
tm.assert_series_equal(result, expected)
