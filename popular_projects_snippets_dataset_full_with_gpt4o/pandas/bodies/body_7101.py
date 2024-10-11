# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH10182
idx = simple_index
idx = idx.repeat(50)
with pd.option_context("display.max_seq_items", None):
    repr(idx)
    assert "..." not in str(idx)
