# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
df = DataFrame(np.random.randn(1000))
labels = np.random.randint(0, 50, size=1000).astype(float)

result = df.groupby(labels)._cython_agg_general(op, alt=None, numeric_only=True)
expected = df.groupby(labels).agg(targop)
tm.assert_frame_equal(result, expected)
