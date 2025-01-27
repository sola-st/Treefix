# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# setting a DataFrame column with a tzaware DTI retains the dtype
df = DataFrame(np.random.randn(2, 1), columns=["A"])

# assign to frame
df["B"] = idx
result = df["B"]
tm.assert_series_equal(result, expected)
