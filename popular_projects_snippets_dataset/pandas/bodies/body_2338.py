# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
ser = Series([1, 2, 3])

mask = np.array([False, False, False])

td = pd.Timedelta(days=1)

res = ser.where(mask, td)
expected = Series([td, td, td], dtype="m8[ns]")
tm.assert_series_equal(res, expected)
