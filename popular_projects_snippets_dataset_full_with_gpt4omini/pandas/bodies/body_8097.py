# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(["a b c", "d e", "f"])
if expand is not None:
    result = index.str.split(expand=expand)
else:
    result = index.str.split()

tm.assert_index_equal(result, expected)
