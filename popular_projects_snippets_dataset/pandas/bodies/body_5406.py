# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#17329
# tz-naive --> treat it as if it were UTC for purposes of timestamp()
ts = fixed_now_ts
uts = ts.replace(tzinfo=utc)
assert ts.timestamp() == uts.timestamp()

tsc = Timestamp("2014-10-11 11:00:01.12345678", tz="US/Central")
utsc = tsc.tz_convert("UTC")

# utsc is a different representation of the same time
assert tsc.timestamp() == utsc.timestamp()

# datetime.timestamp() converts in the local timezone
with tm.set_timezone("UTC"):
    # should agree with datetime.timestamp method
    dt = ts.to_pydatetime()
    assert dt.timestamp() == ts.timestamp()
