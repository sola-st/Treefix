# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
empty = klass(value)
assert isinstance(empty, klass)
assert not len(empty)
