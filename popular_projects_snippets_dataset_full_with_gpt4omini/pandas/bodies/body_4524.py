# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Period analogue to GH#26825
pi = pd.period_range("2016-04-05", periods=3)
data = pi._data.astype(object).reshape(1, -1)
df = DataFrame(data)
assert df.shape == (1, 3)
assert (df.dtypes == pi.dtype).all()
assert (df == pi).all().all()

ii = pd.IntervalIndex.from_breaks([3, 4, 5, 6])
data2 = ii._data.astype(object).reshape(1, -1)
df2 = DataFrame(data2)
assert df2.shape == (1, 3)
assert (df2.dtypes == ii.dtype).all()
assert (df2 == ii).all().all()

# mixed
data3 = np.r_[data, data2, data, data2].T
df3 = DataFrame(data3)
expected = DataFrame({0: pi, 1: ii, 2: pi, 3: ii})
tm.assert_frame_equal(df3, expected)
