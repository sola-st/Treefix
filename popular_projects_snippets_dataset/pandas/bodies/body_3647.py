# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH 18561
df = DataFrame(index=MultiIndex.from_product([range(3), range(3)]))
with pytest.raises(KeyError, match="labels \\[5\\] not found in level"):
    df.drop(5, level=0)
