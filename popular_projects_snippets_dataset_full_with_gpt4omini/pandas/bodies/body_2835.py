# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#23693
# reindex added rows with nan values even when fill method was specified
mi = MultiIndex.from_tuples([("a", "b"), ("d", "e")])
df = DataFrame([[0, 7], [3, 4]], index=mi, columns=["x", "y"])
mi2 = MultiIndex.from_tuples([("a", "b"), ("d", "e"), ("h", "i")])
result = df.reindex(mi2, axis=0, method="ffill")
expected = DataFrame([[0, 7], [3, 4], [3, 4]], index=mi2, columns=["x", "y"])
tm.assert_frame_equal(result, expected)
