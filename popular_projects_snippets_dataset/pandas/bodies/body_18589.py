# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
err_message = (
    "cannot construct a Timedelta from the passed arguments, "
    "allowed keywords are "
    "[weeks, days, hours, minutes, seconds, "
    "milliseconds, microseconds, nanoseconds]"
)

with pytest.raises(ValueError, match=re.escape(err_message)):
    Timedelta(**kwargs)
