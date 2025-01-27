# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# -1 does not get treated as NA unless allow_fill=True is passed
if len(index) == 0:
    # Test is not applicable
    exit()

result = index.take([0, 0, -1])

expected = index.take([0, 0, len(index) - 1])
tm.assert_index_equal(result, expected)
