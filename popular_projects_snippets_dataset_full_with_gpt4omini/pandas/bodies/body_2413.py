# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(np.random.randn(10, 5), index=range(0, 20, 2))

# this is OK
cp = df.copy()
cp.iloc[4:10] = 0
assert (cp.iloc[4:10] == 0).values.all()

# so is this
cp = df.copy()
cp.iloc[3:11] = 0
assert (cp.iloc[3:11] == 0).values.all()

result = df.iloc[2:6]
result2 = df.loc[3:11]
expected = df.reindex([4, 6, 8, 10])

tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(result2, expected)

# non-monotonic, raise KeyError
df2 = df.iloc[list(range(5)) + list(range(5, 10))[::-1]]
with pytest.raises(KeyError, match=r"^3$"):
    df2.loc[3:11]
with pytest.raises(KeyError, match=r"^3$"):
    df2.loc[3:11] = 0
