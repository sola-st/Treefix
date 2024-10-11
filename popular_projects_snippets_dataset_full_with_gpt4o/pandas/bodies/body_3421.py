# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
dta = date_range("2000", periods=8)._data

df = DataFrame({"A": dta[:4]}, copy=False)
df["B"] = dta[4:]

assert len(df._mgr.arrays) == 2

result = df._values
expected = dta.reshape(2, 4).T
tm.assert_equal(result, expected)
