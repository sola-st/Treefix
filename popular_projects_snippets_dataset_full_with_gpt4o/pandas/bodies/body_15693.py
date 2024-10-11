# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py

# check indexes are reordered corresponding with the values
ser = Series([3, 2, 4, 1], ["A", "B", "C", "D"])
expected = Series([1, 2, 3, 4], ["D", "B", "A", "C"])
result = ser.sort_values()
tm.assert_series_equal(expected, result)

ts = datetime_series.copy()
ts[:5] = np.NaN
vals = ts.values

result = ts.sort_values()
assert np.isnan(result[-5:]).all()
tm.assert_numpy_array_equal(result[:-5].values, np.sort(vals[5:]))

# na_position
result = ts.sort_values(na_position="first")
assert np.isnan(result[:5]).all()
tm.assert_numpy_array_equal(result[5:].values, np.sort(vals[5:]))

# something object-type
ser = Series(["A", "B"], [1, 2])
# no failure
ser.sort_values()

# ascending=False
ordered = ts.sort_values(ascending=False)
expected = np.sort(ts.dropna().values)[::-1]
tm.assert_almost_equal(expected, ordered.dropna().values)
ordered = ts.sort_values(ascending=False, na_position="first")
tm.assert_almost_equal(expected, ordered.dropna().values)

# ascending=[False] should behave the same as ascending=False
ordered = ts.sort_values(ascending=[False])
expected = ts.sort_values(ascending=False)
tm.assert_series_equal(expected, ordered)
ordered = ts.sort_values(ascending=[False], na_position="first")
expected = ts.sort_values(ascending=False, na_position="first")
tm.assert_series_equal(expected, ordered)

msg = 'For argument "ascending" expected type bool, received type NoneType.'
with pytest.raises(ValueError, match=msg):
    ts.sort_values(ascending=None)
msg = r"Length of ascending \(0\) must be 1 for Series"
with pytest.raises(ValueError, match=msg):
    ts.sort_values(ascending=[])
msg = r"Length of ascending \(3\) must be 1 for Series"
with pytest.raises(ValueError, match=msg):
    ts.sort_values(ascending=[1, 2, 3])
msg = r"Length of ascending \(2\) must be 1 for Series"
with pytest.raises(ValueError, match=msg):
    ts.sort_values(ascending=[False, False])
msg = 'For argument "ascending" expected type bool, received type str.'
with pytest.raises(ValueError, match=msg):
    ts.sort_values(ascending="foobar")

# inplace=True
ts = datetime_series.copy()
return_value = ts.sort_values(ascending=False, inplace=True)
assert return_value is None
tm.assert_series_equal(ts, datetime_series.sort_values(ascending=False))
tm.assert_index_equal(
    ts.index, datetime_series.sort_values(ascending=False).index
)

# GH#5856/5853
# Series.sort_values operating on a view
df = DataFrame(np.random.randn(10, 4))
s = df.iloc[:, 0]

msg = (
    "This Series is a view of some other array, to sort in-place "
    "you must create a copy"
)
if using_copy_on_write:
    s.sort_values(inplace=True)
    tm.assert_series_equal(s, df.iloc[:, 0].sort_values())
else:
    with pytest.raises(ValueError, match=msg):
        s.sort_values(inplace=True)
