# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# see gh-15414: only boolean arrays accepted
df = DataFrame({"a": [1, 2, 3]})
msg = "Boolean array expected for the condition"

with pytest.raises(ValueError, match=msg):
    df.where(cond)
