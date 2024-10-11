# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(["a", "b"], name="asdf")
assert index.name == index[1:].name
