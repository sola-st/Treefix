# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"a": [True, True]})
r = df.replace([np.inf, -np.inf], np.nan)
e = df
tm.assert_frame_equal(r, e)
