# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
arr = DatetimeArray._from_sequence(
    ["2000"], dtype=DatetimeTZDtype(tz="US/Central")
)
with pytest.raises(AttributeError, match="tz_localize"):
    arr.tz = "UTC"
