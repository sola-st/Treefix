# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# gh43564
result = education_df.groupby("country")[["gender", "education"]].value_counts(
    normalize=True
)
expected = Series(
    data=[0.5, 0.25, 0.25, 0.5, 0.5],
    index=MultiIndex.from_tuples(
        [
            ("FR", "male", "low"),
            ("FR", "female", "high"),
            ("FR", "male", "medium"),
            ("US", "female", "high"),
            ("US", "male", "low"),
        ],
        names=["country", "gender", "education"],
    ),
)
tm.assert_series_equal(result, expected)
