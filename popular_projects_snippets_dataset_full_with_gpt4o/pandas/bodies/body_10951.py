# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH#46357

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

assert_categorical_single_grouper(
    education_df=education_df,
    as_index=as_index,
    observed=True,
    expected_index=expected_index,
    normalize=normalize,
    expected_data=expected_data,
)
