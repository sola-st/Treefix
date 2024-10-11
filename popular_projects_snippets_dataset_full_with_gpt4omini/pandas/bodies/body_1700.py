# Extracted from ./data/repos/pandas/pandas/tests/resample/test_time_grouper.py
# GH 12840
# check TimeGrouper perform stable sorts
n = 20
data = np.random.randn(n, 4)
df = DataFrame(data, columns=["A", "B", "C", "D"])
df["key"] = [
    datetime(2013, 1, 1),
    datetime(2013, 1, 2),
    datetime(2013, 1, 3),
    datetime(2013, 1, 4),
    datetime(2013, 1, 5),
] * 4
grouped = df.groupby(Grouper(key="key", freq="D"))

tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 1)), df[::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 2)), df[1::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 3)), df[2::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 4)), df[3::5])
tm.assert_frame_equal(grouped.get_group(datetime(2013, 1, 5)), df[4::5])
