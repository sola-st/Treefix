# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_astype.py
# https://github.com/pandas-dev/pandas/issues/38607
idx = Index(["あ", b"a"], dtype="object")
result = idx.astype(str)
expected = Index(["あ", "a"], dtype="object")
tm.assert_index_equal(result, expected)
