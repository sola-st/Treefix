# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
# GH10182
idx = idx.repeat(50)
with pd.option_context("display.max_seq_items", None):
    repr(idx)
    assert "..." not in str(idx)
