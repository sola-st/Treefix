# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH 19632
df = DataFrame({"A": [0, 1, 2], "B": [5, np.nan, 7], "C": ["a", "b", "c"]})

result = df.replace(to_replace=to_replace, value=None, method=method)
expected = DataFrame(expected)
tm.assert_frame_equal(result, expected)
