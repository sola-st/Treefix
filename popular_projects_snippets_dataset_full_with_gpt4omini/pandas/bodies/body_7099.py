# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
idx = simple_index
with pytest.raises(TypeError, match="cannot perform all"):
    idx.all()
with pytest.raises(TypeError, match="cannot perform any"):
    idx.any()
