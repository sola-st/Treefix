# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 9107
msg = "Out of bounds nanosecond timestamp"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(dt_str, format="%Y%m%d")
