# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# limit and value
df = DataFrame(np.random.randn(10, 3))
df.iloc[2:7, 0] = np.nan
df.iloc[3:5, 2] = np.nan

expected = df.copy()
expected.iloc[2, 0] = 999
expected.iloc[3, 2] = 999
result = df.fillna(999, limit=1)
tm.assert_frame_equal(result, expected)
