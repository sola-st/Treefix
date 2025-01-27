# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH5508

# len of indexer vs length of the 1d ndarray
df = DataFrame(index=Index(np.arange(1, 11), dtype=np.int64))
df["foo"] = np.zeros(10, dtype=np.float64)
df["bar"] = np.zeros(10, dtype=complex)

# invalid
msg = "Must have equal len keys and value when setting with an iterable"
with pytest.raises(ValueError, match=msg):
    df.loc[df.index[2:5], "bar"] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])

# valid
df.loc[df.index[2:6], "bar"] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])

result = df.loc[df.index[2:6], "bar"]
expected = Series(
    [2.33j, 1.23 + 0.1j, 2.2, 1.0], index=[3, 4, 5, 6], name="bar"
)
tm.assert_series_equal(result, expected)
