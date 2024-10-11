# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
# astype to object series
df = pd.DataFrame({"A": data_missing})
result = df["A"].astype("object")
expected = pd.Series(np.array([np.nan, 1], dtype=object), name="A")
tm.assert_series_equal(result, expected)

# convert to object ndarray
# we assert that we are exactly equal
# including type conversions of scalars
result = df["A"].astype("object").values
expected = np.array([pd.NA, 1], dtype=object)
tm.assert_numpy_array_equal(result, expected)

for r, e in zip(result, expected):
    if pd.isnull(r):
        assert pd.isnull(e)
    elif is_integer(r):
        assert r == e
        assert is_integer(e)
    else:
        assert r == e
        assert type(r) == type(e)
