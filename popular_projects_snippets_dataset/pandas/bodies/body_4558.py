# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
tz = "US/Eastern"
ts = Timestamp("2019", tz=tz)

if box is None or (frame_or_series is DataFrame and box is dict):
    msg = "Cannot unbox tzaware Timestamp to tznaive dtype"
    err = TypeError
else:
    msg = (
        "Cannot convert timezone-aware data to timezone-naive dtype. "
        r"Use pd.Series\(values\).dt.tz_localize\(None\) instead."
    )
    err = ValueError

with pytest.raises(err, match=msg):
    constructor(ts, dtype="M8[ns]")
