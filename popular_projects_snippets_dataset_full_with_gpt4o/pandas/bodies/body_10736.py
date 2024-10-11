# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
df = DataFrame(np.random.randn(1000))
labels = np.random.randint(0, 50, size=1000).astype(float)

result = getattr(df.groupby(labels), op)()
expected = df.groupby(labels).agg(targop)
tm.assert_frame_equal(result, expected)
