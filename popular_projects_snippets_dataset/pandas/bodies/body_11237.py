# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH18432, adapted for GH25871
columns = ["A", "B", "A", "B"]
categories = ["B", "A"]
data = np.array(
    [[1, 2, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2]], int
)
cat_columns = CategoricalIndex(columns, categories=categories, ordered=True)
df = DataFrame(data=data, columns=cat_columns)
result = df.groupby(axis=1, level=0, observed=observed).sum()
expected_data = np.array([[4, 2], [4, 2], [4, 2], [4, 2], [4, 2]], int)
expected_columns = CategoricalIndex(
    categories, categories=categories, ordered=True
)
expected = DataFrame(data=expected_data, columns=expected_columns)
tm.assert_frame_equal(result, expected)

# test transposed version
df = DataFrame(data.T, index=cat_columns)
result = df.groupby(axis=0, level=0, observed=observed).sum()
expected = DataFrame(data=expected_data.T, index=expected_columns)
tm.assert_frame_equal(result, expected)
