# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# GH 40661
labels = [(Timestamp(10),), (Timestamp(20),), (Timestamp(30),)]
result = cut([2, 4, 6], bins=[1, 3, 5, 7], labels=labels)

expected = Categorical.from_codes([0, 1, 2], labels, ordered=True)
tm.assert_categorical_equal(result, expected)
