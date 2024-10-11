# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH6552
index = Index([0, 1, 2])
index.name = name
assert index.reindex(labels)[0].name == name
