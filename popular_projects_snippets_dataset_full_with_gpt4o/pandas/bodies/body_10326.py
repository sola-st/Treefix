# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 33591
df = DataFrame({"data": ["A"], "nans": Series([np.nan], dtype=object)})
grouped = df.groupby("data")

expected = df.set_index("data").nans
tm.assert_series_equal(grouped.nans.first(), expected)
tm.assert_series_equal(grouped.nans.last(), expected)

expected = df.nans
tm.assert_series_equal(grouped.nans.nth(-1), expected)
tm.assert_series_equal(grouped.nans.nth(0), expected)
