# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH26658
s = Series([1, 2, 3])
msg = f"Boolean index has wrong length: {len(index)} instead of {len(s)}"
with pytest.raises(IndexError, match=msg):
    s.iloc[index]
