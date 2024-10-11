# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_formats.py
# GH#35439
idx = Index(["aaaaaaaaa", "b"])
expected = ["aaaaaaaaa", "b"]
assert idx.format() == expected
