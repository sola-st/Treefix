# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#12862 should not raise on assigning the second value
vals = [
    to_datetime(42).tz_localize("UTC"),
    to_datetime(666).tz_localize("UTC"),
]
expected = Series(vals, index=["foo", "bar"])

ser = Series(dtype=object)
indexer_sl(ser)["foo"] = vals[0]
indexer_sl(ser)["bar"] = vals[1]

tm.assert_series_equal(ser, expected)
