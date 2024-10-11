# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_equivalence.py
# GH9785
assert (idx == idx).all()
