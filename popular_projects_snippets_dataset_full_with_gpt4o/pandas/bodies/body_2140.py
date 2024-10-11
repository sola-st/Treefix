# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
values = [1420043460000, iNaT, NaT, np.nan, "NaT"]

result = to_datetime(values, errors="ignore", unit="s", cache=cache)
expected = Index([1420043460000, NaT, NaT, NaT, NaT], dtype=object)
tm.assert_index_equal(result, expected)

result = to_datetime(values, errors="coerce", unit="s", cache=cache)
expected = DatetimeIndex(["NaT", "NaT", "NaT", "NaT", "NaT"])
tm.assert_index_equal(result, expected)

msg = "cannot convert input 1420043460000 with the unit 's'"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(values, errors="raise", unit="s", cache=cache)
