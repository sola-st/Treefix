# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
idx = MultiIndex.from_product([["a"], [1, 2]], names=["a", "b"])

assert idx.levels[0].name == "a"
assert idx.levels[1].name == "b"
