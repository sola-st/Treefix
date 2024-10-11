# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# see gh-12077
# constructor with a datetimelike and NaT

s = Series(dtl)
c = Categorical(s)

expected = type(dtl)(s)
expected._data.freq = None

tm.assert_index_equal(c.categories, expected)
tm.assert_numpy_array_equal(c.codes, np.arange(5, dtype="int8"))

# with NaT
s2 = s.copy()
s2.iloc[-1] = NaT
c = Categorical(s2)

expected = type(dtl)(s2.dropna())
expected._data.freq = None

tm.assert_index_equal(c.categories, expected)

exp = np.array([0, 1, 2, 3, -1], dtype=np.int8)
tm.assert_numpy_array_equal(c.codes, exp)

result = repr(c)
assert "NaT" in result
