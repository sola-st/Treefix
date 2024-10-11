# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
# construct from our dtype & string dtype
dtype = data.dtype

# from float
expected = pd.Series(data)
result = pd.Series(data.to_numpy(na_value=np.nan, dtype="float"), dtype=str(dtype))
tm.assert_series_equal(result, expected)

# from list
expected = pd.Series(data)
result = pd.Series(np.array(data).tolist(), dtype=str(dtype))
tm.assert_series_equal(result, expected)
