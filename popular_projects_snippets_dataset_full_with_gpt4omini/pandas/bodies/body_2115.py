# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH24763
with tm.assert_produces_warning(warning, match="Could not infer format"):
    res = to_datetime(value, errors="ignore", format=format)
assert res == value

with tm.assert_produces_warning(warning, match="Could not infer format"):
    res = to_datetime(value, errors="coerce", format=format)
assert res is NaT

if format is not None:
    msg = r'^time data ".*" doesn\'t match format ".*", at position 0$'
    with pytest.raises(ValueError, match=msg):
        to_datetime(value, errors="raise", format=format)
else:
    msg = "^Out of bounds .*, at position 0$"
    with pytest.raises(
        OutOfBoundsDatetime, match=msg
    ), tm.assert_produces_warning(warning, match="Could not infer format"):
        to_datetime(value, errors="raise", format=format)
