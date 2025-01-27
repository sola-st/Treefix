# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-16459
arr = [50, 5, 10, 15, 20, 30, 70]
labels = ["Good", "Medium", "Bad"]

result = cut(arr, 3, labels=labels)
exp = cut(arr, 3, labels=Categorical(labels, categories=labels, ordered=True))
tm.assert_categorical_equal(result, exp)
