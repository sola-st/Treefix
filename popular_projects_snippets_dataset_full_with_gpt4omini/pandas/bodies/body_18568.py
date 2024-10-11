# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
# see gh-17697
data = ["2015-11-18 15:30:00+05:30", "2015-11-18 15:30:00+06:30"]
data = np.array(data, dtype=object)

result, result_tz = tslib.array_to_datetime(data)
expected = np.array(
    [
        datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 19800)),
        datetime(2015, 11, 18, 15, 30, tzinfo=tzoffset(None, 23400)),
    ],
    dtype=object,
)

tm.assert_numpy_array_equal(result, expected)
assert result_tz is None
