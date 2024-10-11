# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
indices = datetime_series.index[[5, 10, 15]]

cp = datetime_series.copy()
exp = datetime_series.copy()
cp[indices] = 0
exp.loc[indices] = 0
tm.assert_series_equal(cp, exp)

cp = datetime_series.copy()
exp = datetime_series.copy()
cp[indices[0] : indices[2]] = 0
exp.loc[indices[0] : indices[2]] = 0
tm.assert_series_equal(cp, exp)
