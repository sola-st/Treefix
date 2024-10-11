# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
df1 = DataFrame(np.random.randn(0, 3))
df2 = DataFrame(np.random.randn(0, 3))
df1.index.name = "foo"
assert df2.index.name is None
