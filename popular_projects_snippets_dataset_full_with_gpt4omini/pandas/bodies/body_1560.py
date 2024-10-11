# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#13691
mi = MultiIndex.from_product([[0], [1, 1]])
ser = Series(0, index=mi)

res = ser.loc[[]]

expected = ser[:0]
tm.assert_series_equal(res, expected)

res2 = ser.loc[ser.iloc[0:0]]
tm.assert_series_equal(res2, expected)
