# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# Test single categorical grouper when non-groupers are also categorical
education_df = education_df.copy().astype("category")

# Add non-observed grouping categories
education_df["country"] = education_df["country"].cat.add_categories(["ASIA"])

gp = education_df.groupby("country", as_index=as_index, observed=observed)
result = gp.value_counts(normalize=normalize)

expected_series = Series(
    data=expected_data,
    index=MultiIndex.from_tuples(
        expected_index,
        names=["country", "gender", "education"],
    ),
)
for i in range(3):
    index_level = CategoricalIndex(expected_series.index.levels[i])
    if i == 0:
        index_level = index_level.set_categories(
            education_df["country"].cat.categories
        )
    expected_series.index = expected_series.index.set_levels(index_level, level=i)

if as_index:
    tm.assert_series_equal(result, expected_series)
else:
    expected = expected_series.reset_index(
        name="proportion" if normalize else "count"
    )
    tm.assert_frame_equal(result, expected)
