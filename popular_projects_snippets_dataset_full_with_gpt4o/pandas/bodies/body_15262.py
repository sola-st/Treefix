# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# GH 17610
result = result_1._append(duplicate_item)
expected = expected_1._append(duplicate_item)
tm.assert_series_equal(result[1], expected)
assert result[2] == result_1[2]
