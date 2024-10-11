# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
s = Series(np.arange(6))
k1 = np.array(["a", "a", "a", "b", "b", "b"])
k2 = np.array(["1", "2", "1", "2", "1", "2"])

grouped = s.groupby([k1, k2])

iterated = list(grouped)
expected = [
    ("a", "1", s[[0, 2]]),
    ("a", "2", s[[1]]),
    ("b", "1", s[[4]]),
    ("b", "2", s[[3, 5]]),
]
for i, ((one, two), three) in enumerate(iterated):
    e1, e2, e3 = expected[i]
    assert e1 == one
    assert e2 == two
    tm.assert_series_equal(three, e3)
