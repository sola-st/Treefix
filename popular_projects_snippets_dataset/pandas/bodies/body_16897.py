# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# GH 13318
values = range(3)
result = qcut(values, 3, labels=labels)
tm.assert_categorical_equal(result, expected)
