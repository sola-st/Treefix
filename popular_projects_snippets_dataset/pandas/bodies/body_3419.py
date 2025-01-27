# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
dta = date_range("2000", periods=4, tz="US/Central")._data.reshape(-1, 1)

df = DataFrame(dta, columns=["A"])
tm.assert_equal(df._values, dta)

# we have a view
assert np.shares_memory(df._values._ndarray, dta._ndarray)

# TimedeltaArray
tda = dta - dta
df2 = df - df
tm.assert_equal(df2._values, tda)
