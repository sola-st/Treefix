# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py

# GH4746, reindex on duplicate index error messages
arr = np.random.randn(10)
df = DataFrame(arr, index=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5])

# set index is ok
result = df.copy()
result.index = list(range(len(df)))
expected = DataFrame(arr, index=list(range(len(df))))
tm.assert_frame_equal(result, expected)

# reindex fails
msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    df.reindex(index=list(range(len(df))))
