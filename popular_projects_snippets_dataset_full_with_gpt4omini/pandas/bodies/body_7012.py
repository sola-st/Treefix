# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_formats.py
# GH#35439
idx = CategoricalIndex(["aaaaaaaaa", "b"])
expected = ["aaaaaaaaa", "b"]
assert idx.format() == expected
