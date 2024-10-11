# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
df = DataFrame({"A": [1, np.nan], "B": [1.0, 2.0]})
expected = df.replace(np.nan, val)
result = df.fillna(val)
tm.assert_frame_equal(result, expected)
