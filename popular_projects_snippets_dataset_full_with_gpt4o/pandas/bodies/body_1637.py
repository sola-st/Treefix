# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
ser = Series(np.random.randn(10), index=list(range(0, 20, 2)))

# this is OK
cp = ser.copy()
cp.iloc[4:10] = 0
assert (cp.iloc[4:10] == 0).all()

# so is this
cp = ser.copy()
cp.iloc[3:11] = 0
assert (cp.iloc[3:11] == 0).values.all()

result = ser.iloc[2:6]
result2 = ser.loc[3:11]
expected = ser.reindex([4, 6, 8, 10])

tm.assert_series_equal(result, expected)
tm.assert_series_equal(result2, expected)

# non-monotonic, raise KeyError
s2 = ser.iloc[list(range(5)) + list(range(9, 4, -1))]
with pytest.raises(KeyError, match=r"^3$"):
    s2.loc[3:11]
with pytest.raises(KeyError, match=r"^3$"):
    s2.loc[3:11] = 0
