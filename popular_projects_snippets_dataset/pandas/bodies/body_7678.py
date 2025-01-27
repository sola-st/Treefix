# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH 15110 and GH 14848

li = [(0, 0, 1), (0, 1, 0), (1, 0, 0)]
msg = "Names should be list-like for a MultiIndex"
with pytest.raises(ValueError, match=msg):
    Index(li, name="abc")
with pytest.raises(ValueError, match=msg):
    Index(li, name="a")
