# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
values = [11111111, 1, 1.0, iNaT, NaT, np.nan, "NaT", ""]
result = to_datetime(values, unit="D", errors="ignore", cache=cache)
expected = Index(
    [
        11111111,
        Timestamp("1970-01-02"),
        Timestamp("1970-01-02"),
        NaT,
        NaT,
        NaT,
        NaT,
        NaT,
    ],
    dtype=object,
)
tm.assert_index_equal(result, expected)

result = to_datetime(values, unit="D", errors="coerce", cache=cache)
expected = DatetimeIndex(
    ["NaT", "1970-01-02", "1970-01-02", "NaT", "NaT", "NaT", "NaT", "NaT"]
)
tm.assert_index_equal(result, expected)

msg = "cannot convert input 11111111 with the unit 'D'"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(values, unit="D", errors="raise", cache=cache)
