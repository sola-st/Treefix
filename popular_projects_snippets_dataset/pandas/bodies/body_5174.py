# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_constructors.py
# ignore the unit, as it may cause silently overflows leading to incorrect
#  results, and in non-overflow cases is irrelevant GH#46827
obj = np.timedelta64(123456789000000000, "h")

with pytest.raises(OutOfBoundsTimedelta, match="123456789000000000 hours"):
    Timedelta(obj, unit="ps")

with pytest.raises(OutOfBoundsTimedelta, match="123456789000000000 hours"):
    Timedelta(obj, unit="ns")

with pytest.raises(OutOfBoundsTimedelta, match="123456789000000000 hours"):
    Timedelta(obj)
