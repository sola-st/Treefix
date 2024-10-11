# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
dtype = any_int_numpy_dtype
ser = Series(np.random.randn(6), index=Index([0, 0, 1, 1, 2, 2], dtype=dtype))

with pytest.raises(KeyError, match=r"^5$"):
    ser[5]

with pytest.raises(KeyError, match=r"^'c'$"):
    ser["c"]

# not monotonic
ser = Series(np.random.randn(6), index=[2, 2, 0, 0, 1, 1])

with pytest.raises(KeyError, match=r"^5$"):
    ser[5]

with pytest.raises(KeyError, match=r"^'c'$"):
    ser["c"]
