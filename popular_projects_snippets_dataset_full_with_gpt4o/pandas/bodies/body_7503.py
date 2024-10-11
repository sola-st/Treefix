# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
# GH1538
with pd.option_context("display.multi_sparse", False):
    result = idx.format()
assert result[1] == "foo  two"
