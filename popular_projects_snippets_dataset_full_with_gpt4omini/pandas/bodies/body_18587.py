# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
msg = (
    "delta_to_nanoseconds does not support Y or M units, "
    "as their duration in nanoseconds is ambiguous"
)

td = np.timedelta64(1234, "Y")

with pytest.raises(ValueError, match=msg):
    delta_to_nanoseconds(td)

td = np.timedelta64(1234, "M")

with pytest.raises(ValueError, match=msg):
    delta_to_nanoseconds(td)
