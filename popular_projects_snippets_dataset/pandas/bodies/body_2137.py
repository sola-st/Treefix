# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#50301
# Match Timestamp behavior in disallowing non-round floats with
#  Y or M unit
msg = f"Conversion of non-round float with unit={unit} is ambiguous"
with pytest.raises(ValueError, match=msg):
    to_datetime([1.5], unit=unit, errors="raise")
with pytest.raises(ValueError, match=msg):
    to_datetime(["1.5"], unit=unit, errors="raise")

# with errors="ignore" we also end up raising within the Timestamp
#  constructor; this may not be ideal
with pytest.raises(ValueError, match=msg):
    to_datetime([1.5], unit=unit, errors="ignore")
# TODO: we are NOT consistent with the Timestamp behavior in the
#  float-like string case
# with pytest.raises(ValueError, match=msg):
#    to_datetime(["1.5"], unit=unit, errors="ignore")

res = to_datetime([1.5], unit=unit, errors="coerce")
expected = Index([NaT], dtype="M8[ns]")
tm.assert_index_equal(res, expected)

res = to_datetime(["1.5"], unit=unit, errors="coerce")
tm.assert_index_equal(res, expected)

# round floats are OK
res = to_datetime([1.0], unit=unit)
expected = to_datetime([1], unit=unit)
tm.assert_index_equal(res, expected)
