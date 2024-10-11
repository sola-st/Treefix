# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH-42843
result = np.array([np.nan, 1, np.nan])
expected = result.copy()
ser = Series([1, 2, 3])

# Test numpy array weights won't be modified in place
ser.sample(weights=result)
tm.assert_numpy_array_equal(result, expected)

# Test DataFrame column won't be modified in place
df = DataFrame({"values": [1, 1, 1], "weights": [1, np.nan, np.nan]})
expected = df["weights"].copy()

df.sample(frac=1.0, replace=True, weights="weights")
result = df["weights"]
tm.assert_series_equal(result, expected)
