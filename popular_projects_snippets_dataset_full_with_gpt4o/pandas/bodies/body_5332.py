# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# GH#19643, used to incorrectly give Timestamp in 1754
per = Period("0001-01-01", freq="B")
msg = "Out of bounds nanosecond timestamp"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    per.to_timestamp()
