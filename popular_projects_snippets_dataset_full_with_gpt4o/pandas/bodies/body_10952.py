# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH#46357

expected_index = [
    ("FR", "male", "low"),
    ("FR", "female", "high"),
    ("FR", "male", "medium"),
    ("FR", "female", "low"),
    ("FR", "male", "high"),
    ("FR", "female", "medium"),
    ("US", "female", "high"),
    ("US", "male", "low"),
    ("US", "male", "medium"),
    ("US", "male", "high"),
    ("US", "female", "medium"),
    ("US", "female", "low"),
    ("ASIA", "male", "low"),
    ("ASIA", "male", "high"),
    ("ASIA", "female", "medium"),
    ("ASIA", "female", "low"),
    ("ASIA", "female", "high"),
    ("ASIA", "male", "medium"),
]

assert_categorical_single_grouper(
    education_df=education_df,
    as_index=as_index,
    observed=False,
    expected_index=expected_index,
    normalize=normalize,
    expected_data=expected_data,
)
