# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
s = Series(np.random.randn(5), index=["a", "b", "a", "a", "b"])

msg = "index 5 is out of bounds for axis 0 with size 5"
with pytest.raises(IndexError, match=msg):
    s[5]
with pytest.raises(IndexError, match=msg):
    s[5] = 0

with pytest.raises(KeyError, match=r"^'c'$"):
    s["c"]

s = s.sort_index()

with pytest.raises(IndexError, match=msg):
    s[5]
msg = r"index 5 is out of bounds for axis (0|1) with size 5|^5$"
with pytest.raises(IndexError, match=msg):
    s[5] = 0
