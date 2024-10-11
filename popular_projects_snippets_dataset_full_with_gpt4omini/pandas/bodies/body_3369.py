# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame({"A": [np.nan, 1]})
res1 = df.replace(to_replace={np.nan: 0, 1: -1e8})
res2 = df.replace(to_replace=(1, np.nan), value=[-1e8, 0])
res3 = df.replace(to_replace=[1, np.nan], value=[-1e8, 0])

expected = DataFrame({"A": [0, -1e8]})
tm.assert_frame_equal(res1, res2)
tm.assert_frame_equal(res2, res3)
tm.assert_frame_equal(res3, expected)
