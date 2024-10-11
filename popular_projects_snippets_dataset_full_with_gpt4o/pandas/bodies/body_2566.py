# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# setting a DataFrame column with a tzaware DTI retains the dtype
df = DataFrame(np.random.randn(2, 1), columns=["A"])

# object array of datetimes with a tz
df["B"] = idx.to_pydatetime()
result = df["B"]
tm.assert_series_equal(result, expected)
