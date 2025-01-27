# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
# this is an invalid subtype
msg = (
    "Incorrectly formatted string passed to constructor. "
    r"Valid formats include Interval or Interval\[dtype\] "
    "where dtype is numeric, datetime, or timedelta"
)

with pytest.raises(TypeError, match=msg):
    IntervalDtype.construct_from_string(string)
