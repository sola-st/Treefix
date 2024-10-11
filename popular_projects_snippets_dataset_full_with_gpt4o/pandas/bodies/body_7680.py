# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# 0 levels
msg = "Must pass non-zero number of levels/codes"
with pytest.raises(ValueError, match=msg):
    MultiIndex.from_product([])
