# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
arr = period_array(["2000", "2001"], freq="D")

msg = str(arr[0].ordinal)
with pytest.raises(TypeError, match=msg):
    PeriodArray._from_sequence(arr.asi8, dtype=arr.dtype)

with pytest.raises(TypeError, match=msg):
    PeriodArray._from_sequence(list(arr.asi8), dtype=arr.dtype)
