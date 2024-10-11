# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# time not supported ATM
msg = (
    "Value must be Timedelta, string, integer, float, timedelta or convertible"
)
with pytest.raises(ValueError, match=msg):
    to_timedelta(time(second=1))
assert to_timedelta(time(second=1), errors="coerce") is pd.NaT
