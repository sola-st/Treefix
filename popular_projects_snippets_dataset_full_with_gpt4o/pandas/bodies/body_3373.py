# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
df = DataFrame(np.random.rand(2, 2) > 0.5)
result = df.replace(False, True)
expected = DataFrame(np.ones((2, 2), dtype=bool))
tm.assert_frame_equal(result, expected)
