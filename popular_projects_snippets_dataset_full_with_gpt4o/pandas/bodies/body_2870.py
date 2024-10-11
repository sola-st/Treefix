# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
df = DataFrame(np.random.randn(10, 10))
df.values[:, ::2] = np.nan

result = df.fillna(method="ffill", axis=1)
expected = df.T.fillna(method="pad").T
tm.assert_frame_equal(result, expected)

df.insert(6, "foo", 5)
result = df.fillna(method="ffill", axis=1)
expected = df.astype(float).fillna(method="ffill", axis=1)
tm.assert_frame_equal(result, expected)
