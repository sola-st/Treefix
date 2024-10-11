# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_get.py
# GH#7725
d0 = ["a", "b", "c", "d"]
d1 = np.arange(4, dtype="int64")
others = ["e", 10]

for data, index in ((d0, d1), (d1, d0)):
    s = Series(data, index=index)
    for i, d in zip(index, data):
        assert s.get(i) == d
        assert s.get(i, d) == d
        assert s.get(i, "z") == d
        for other in others:
            assert s.get(other, "z") == "z"
            assert s.get(other, other) == other
