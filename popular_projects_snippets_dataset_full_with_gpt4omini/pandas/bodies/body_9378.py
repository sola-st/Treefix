# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
# construct from our dtype & string dtype
dtype = data.dtype

# from float
expected = pd.Series(data)
result = pd.Series(data.to_numpy(na_value=np.nan, dtype="float"), dtype=str(dtype))
tm.assert_series_equal(result, expected)

# from int / list
expected = pd.Series(data)
result = pd.Series(np.array(data).tolist(), dtype=str(dtype))
tm.assert_series_equal(result, expected)

# from int / array
expected = pd.Series(data).dropna().reset_index(drop=True)
dropped = np.array(data.dropna()).astype(np.dtype(dtype.type))
result = pd.Series(dropped, dtype=str(dtype))
tm.assert_series_equal(result, expected)
