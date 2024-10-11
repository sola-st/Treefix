# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# see gh-15630.

df = DataFrame([[2012, 66, 3], [2012, 65, 2], [2012, 65, 1]])
result = df.rank(method=method, pct=True)

expected = DataFrame(exp)
tm.assert_frame_equal(result, expected)
