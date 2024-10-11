# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# GH-37867
# na value handling in Categorical.__contains__ is deprecated.
# See base.BaseInterFaceTests.test_contains for more details.

na_value = data.dtype.na_value
# ensure data without missing values
data = data[~data.isna()]

# first elements are non-missing
assert data[0] in data
assert data_missing[0] in data_missing

# check the presence of na_value
assert na_value in data_missing
assert na_value not in data

# Categoricals can contain other nan-likes than na_value
for na_value_obj in tm.NULL_OBJECTS:
    if na_value_obj is na_value:
        continue
    assert na_value_obj not in data
    assert na_value_obj in data_missing  # this line differs from super method
