# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(np.random.rand(2, 2) > 0.5)
result = df.replace("asdf", "fdsa")
tm.assert_frame_equal(df, result)
