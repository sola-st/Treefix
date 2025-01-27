# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH 7729
# make sure we are boxing the returns
result = indexer_ial(ser)[1]
assert result == expected
