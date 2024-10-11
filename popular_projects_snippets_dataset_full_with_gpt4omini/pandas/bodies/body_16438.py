# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
data = [np.datetime64("2012-12-13"), np.datetime64("2012-12-15")]
bin_data = ["2012-12-12", "2012-12-14", "2012-12-16"]

expected = Series(
    IntervalIndex(
        [
            Interval(Timestamp(bin_data[0]), Timestamp(bin_data[1])),
            Interval(Timestamp(bin_data[1]), Timestamp(bin_data[2])),
        ]
    )
).astype(CDT(ordered=True))

bins = [conv(v) for v in bin_data]
result = Series(cut(data, bins=bins))
tm.assert_series_equal(result, expected)
