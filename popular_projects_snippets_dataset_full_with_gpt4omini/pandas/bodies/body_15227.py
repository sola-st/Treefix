# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_where.py
# see gh-15414: only boolean arrays accepted
s = Series([1, 2, 3])
msg = "Boolean array expected for the condition"

with pytest.raises(ValueError, match=msg):
    s.where(cond)

msg = "Array conditional must be same shape as self"
with pytest.raises(ValueError, match=msg):
    s.where([True])
