# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH39401
result = RI.append([])
tm.assert_index_equal(result, RI, exact=True)
