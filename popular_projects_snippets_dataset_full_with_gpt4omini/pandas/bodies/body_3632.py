# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH# 21494
with pytest.raises(KeyError, match="not found in axis"):
    DataFrame(index=index).drop(drop_labels)
