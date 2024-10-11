# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py

# Test single categorical grouper with only observed grouping categories
# when non-groupers are also categorical

gp = education_df.astype("category").groupby(
    "country", as_index=as_index, observed=observed
)
result = gp.value_counts(normalize=normalize)

expected_index = MultiIndex.from_tuples(
    [
        ("FR", "male", "low"),
        ("FR", "female", "high"),
        ("FR", "male", "medium"),
        ("FR", "female", "low"),
        ("FR", "female", "medium"),
        ("FR", "male", "high"),
        ("US", "female", "high"),
        ("US", "male", "low"),
        ("US", "female", "low"),
        ("US", "female", "medium"),
        ("US", "male", "high"),
        ("US", "male", "medium"),
    ],
    names=["country", "gender", "education"],
)

expected_series = Series(
    data=expected_data,
    index=expected_index,
)
for i in range(3):
    expected_series.index = expected_series.index.set_levels(
        CategoricalIndex(expected_series.index.levels[i]), level=i
    )

if as_index:
    tm.assert_series_equal(result, expected_series)
else:
    expected = expected_series.reset_index(
        name="proportion" if normalize else "count"
    )
    tm.assert_frame_equal(result, expected)
