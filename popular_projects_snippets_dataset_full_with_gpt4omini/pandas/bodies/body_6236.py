# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
# GH-37867
# Tests for membership checks. Membership checks for nan-likes is tricky and
# the settled on rule is: `nan_like in arr` is True if nan_like is
# arr.dtype.na_value and arr.isna().any() is True. Else the check returns False.

na_value = data.dtype.na_value
# ensure data without missing values
data = data[~data.isna()]

# first elements are non-missing
assert data[0] in data
assert data_missing[0] in data_missing

# check the presence of na_value
assert na_value in data_missing
assert na_value not in data

# the data can never contain other nan-likes than na_value
for na_value_obj in tm.NULL_OBJECTS:
    if na_value_obj is na_value or type(na_value_obj) == type(na_value):
        # type check for e.g. two instances of Decimal("NAN")
        continue
    assert na_value_obj not in data
    assert na_value_obj not in data_missing
