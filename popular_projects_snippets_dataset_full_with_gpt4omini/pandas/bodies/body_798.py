# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
left = nulls_fixture
right = nulls_fixture2

assert libmissing.is_matching_na(left, left)

if left is right:
    assert libmissing.is_matching_na(left, right)
elif is_float(left) and is_float(right):
    # np.nan vs float("NaN") we consider as matching
    assert libmissing.is_matching_na(left, right)
elif type(left) is type(right):
    # e.g. both Decimal("NaN")
    assert libmissing.is_matching_na(left, right)
else:
    assert not libmissing.is_matching_na(left, right)
