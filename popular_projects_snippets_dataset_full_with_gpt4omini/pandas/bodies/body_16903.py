# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# issue 20303
data_expected = box([0, 1, 1, 0, 1] * 10)
data_result = box([False, True, True, False, True] * 10)
expected = qcut(data_expected, bins, duplicates="drop")
result = qcut(data_result, bins, duplicates="drop")
compare(result, expected)
