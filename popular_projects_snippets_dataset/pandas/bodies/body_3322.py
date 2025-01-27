# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# GH#32593
df = DataFrame({"a": [-np.inf, 0, np.inf]})
expected = DataFrame({"a": [1.0, 2.0, 3.0]})
result = df.rank()
tm.assert_frame_equal(result, expected)
