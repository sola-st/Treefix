# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH 8594
mi = MultiIndex.from_arrays([[1, 2, 3], [4, 5, 6]], names=["a", "b"])
s = Series([10, 20, 30], index=mi)
df = DataFrame([10, 20, 30], index=mi)

with pytest.raises(KeyError, match=msg):
    s.drop(labels, level=level)
with pytest.raises(KeyError, match=msg):
    df.drop(labels, level=level)
