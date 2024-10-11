# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
bins = [0, 25, 50, 100]
arr = [50, 5, 10, 15, 20, 30, 70]
labels = ["Small", "Medium", "Large"]

result = cut(arr, bins, labels=get_labels(labels))
tm.assert_categorical_equal(result, get_expected(labels))
