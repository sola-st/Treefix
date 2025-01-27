# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH38672

s = Series(Categorical(["a"], categories=["a", "b"]))
result = s.groupby([0]).value_counts()

expected = Series(
    data=[1, 0],
    index=MultiIndex.from_arrays(
        [
            np.array([0, 0]),
            CategoricalIndex(
                ["a", "b"], categories=["a", "b"], ordered=False, dtype="category"
            ),
        ]
    ),
)

# Expected:
# 0  a    1
#    b    0
# dtype: int64

tm.assert_series_equal(result, expected)
