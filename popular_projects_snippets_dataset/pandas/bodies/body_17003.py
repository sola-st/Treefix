# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH 16111, categories that aren't lexsorted
categories = [9, 0, 1, 2, 3]

a = Series(1, index=pd.CategoricalIndex([9, 0], categories=categories))
b = Series(2, index=pd.CategoricalIndex([0, 1], categories=categories))
c = Series(3, index=pd.CategoricalIndex([1, 2], categories=categories))

result = pd.concat([a, b, c], axis=1)

exp_idx = pd.CategoricalIndex([9, 0, 1, 2], categories=categories)
exp = DataFrame(
    {
        0: [1, 1, np.nan, np.nan],
        1: [np.nan, 2, 2, np.nan],
        2: [np.nan, np.nan, 3, 3],
    },
    columns=[0, 1, 2],
    index=exp_idx,
)
tm.assert_frame_equal(result, exp)
