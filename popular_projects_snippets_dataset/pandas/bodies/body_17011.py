# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# https://github.com/pandas-dev/pandas/issues/24845

c1 = pd.CategoricalIndex(["a", "a"], categories=["a", "b"], ordered=False)
c2 = pd.CategoricalIndex(["b", "b"], categories=["b", "a"], ordered=False)
c3 = pd.CategoricalIndex(
    ["a", "a", "b", "b"], categories=["a", "b"], ordered=False
)

df1 = DataFrame({"A": [1, 2]}, index=c1)
df2 = DataFrame({"A": [3, 4]}, index=c2)

result = pd.concat((df1, df2))
expected = DataFrame({"A": [1, 2, 3, 4]}, index=c3)
tm.assert_frame_equal(result, expected)
