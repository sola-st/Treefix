# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index([5, datetime.now(), 7])
assert not getattr(index, attr)
