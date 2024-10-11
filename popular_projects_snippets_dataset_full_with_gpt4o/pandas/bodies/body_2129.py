# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 17697, 11736
ts_strings = ["2015-11-18 15:30:00+05:30", "2015-11-18 16:30:00+06:30", NaT]
result = to_datetime(ts_strings)
expected = np.array(
    [
        datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 19800)),
        datetime(2015, 11, 18, 16, 30, tzinfo=tzoffset(None, 23400)),
        NaT,
    ],
    dtype=object,
)
# GH 21864
expected = Index(expected)
tm.assert_index_equal(result, expected)
