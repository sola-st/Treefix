# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#42376
# for use-case df["x"] = sparse.random(10, 10).mean(axis=1)
expected = DataFrame(
    {"np-array": np.ones(10), "np-matrix": np.ones(10)}, index=np.arange(10)
)

a = np.ones((10, 1))
df = DataFrame(index=np.arange(10))
df["np-array"] = a

# Instantiation of `np.matrix` gives PendingDeprecationWarning
with tm.assert_produces_warning(PendingDeprecationWarning):
    df["np-matrix"] = np.matrix(a)

tm.assert_frame_equal(df, expected)
