# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
df = tm.makeDataFrame()[:5]
ser = df.stack()
ser.index.names = ["hash", "category"]

ser.name = "value"
df = ser.reset_index()
assert "value" in df

df = ser.reset_index(name="value2")
assert "value2" in df

# check inplace
s = ser.reset_index(drop=True)
s2 = ser
return_value = s2.reset_index(drop=True, inplace=True)
assert return_value is None
tm.assert_series_equal(s, s2)

# level
index = MultiIndex(
    levels=[["bar"], ["one", "two", "three"], [0, 1]],
    codes=[[0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]],
)
s = Series(np.random.randn(6), index=index)
rs = s.reset_index(level=1)
assert len(rs.columns) == 2

rs = s.reset_index(level=[0, 2], drop=True)
tm.assert_index_equal(rs.index, Index(index.get_level_values(1)))
assert isinstance(rs, Series)
