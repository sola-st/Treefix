# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
df = DataFrame(
    np.random.randn(10, 4), columns=[["a", "a", "b", "b"], [0, 1, 0, 1]]
)

cp = df.copy()
cp["a"] = cp["b"]
tm.assert_frame_equal(cp["a"], cp["b"])

# set with ndarray
cp = df.copy()
cp["a"] = cp["b"].values
tm.assert_frame_equal(cp["a"], cp["b"])
