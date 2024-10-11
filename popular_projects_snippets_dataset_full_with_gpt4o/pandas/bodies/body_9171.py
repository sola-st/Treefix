# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_api.py
# string type
desc = factor.describe()
assert factor.ordered
exp_index = CategoricalIndex(
    ["a", "b", "c"], name="categories", ordered=factor.ordered
)
expected = DataFrame(
    {"counts": [3, 2, 3], "freqs": [3 / 8.0, 2 / 8.0, 3 / 8.0]}, index=exp_index
)
tm.assert_frame_equal(desc, expected)

# check unused categories
cat = factor.copy()
cat = cat.set_categories(["a", "b", "c", "d"])
desc = cat.describe()

exp_index = CategoricalIndex(
    list("abcd"), ordered=factor.ordered, name="categories"
)
expected = DataFrame(
    {"counts": [3, 2, 3, 0], "freqs": [3 / 8.0, 2 / 8.0, 3 / 8.0, 0]},
    index=exp_index,
)
tm.assert_frame_equal(desc, expected)

# check an integer one
cat = Categorical([1, 2, 3, 1, 2, 3, 3, 2, 1, 1, 1])
desc = cat.describe()
exp_index = CategoricalIndex([1, 2, 3], ordered=cat.ordered, name="categories")
expected = DataFrame(
    {"counts": [5, 3, 3], "freqs": [5 / 11.0, 3 / 11.0, 3 / 11.0]},
    index=exp_index,
)
tm.assert_frame_equal(desc, expected)

# https://github.com/pandas-dev/pandas/issues/3678
# describe should work with NaN
cat = Categorical([np.nan, 1, 2, 2])
desc = cat.describe()
expected = DataFrame(
    {"counts": [1, 2, 1], "freqs": [1 / 4.0, 2 / 4.0, 1 / 4.0]},
    index=CategoricalIndex(
        [1, 2, np.nan], categories=[1, 2], name="categories"
    ),
)
tm.assert_frame_equal(desc, expected)
