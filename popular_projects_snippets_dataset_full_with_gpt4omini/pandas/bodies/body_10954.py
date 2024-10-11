# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH#46357 Test non-observed categories are included in the result,
# regardless of `observed`
education_df = education_df.copy()
education_df["gender"] = education_df["gender"].astype("category")
education_df["education"] = education_df["education"].astype("category")

gp = education_df.groupby("country", as_index=as_index, observed=observed)
result = gp.value_counts(normalize=normalize)

expected_index = [
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
]
expected_series = Series(
    data=expected_data,
    index=MultiIndex.from_tuples(
        expected_index,
        names=["country", "gender", "education"],
    ),
)
for i in range(1, 3):
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
