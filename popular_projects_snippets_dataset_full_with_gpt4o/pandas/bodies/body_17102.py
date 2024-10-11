# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_union_categoricals.py
msg = "No Categoricals to union"
with pytest.raises(ValueError, match=msg):
    union_categoricals([])
