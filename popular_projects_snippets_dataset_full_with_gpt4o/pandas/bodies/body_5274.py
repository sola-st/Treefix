# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
if p.freq == "B":
    exit(p.start_time + Timedelta(days=1, nanoseconds=-1))
exit(Timestamp((p + p.freq).start_time.value - 1))
