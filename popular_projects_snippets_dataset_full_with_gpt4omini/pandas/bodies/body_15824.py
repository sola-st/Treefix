# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
s = Series([0, 1])
s.rank(method="average")
msg = "No axis named average for object type Series"
with pytest.raises(ValueError, match=msg):
    s.rank("average")
