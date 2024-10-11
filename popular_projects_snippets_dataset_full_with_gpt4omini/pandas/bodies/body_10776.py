# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
if isinstance(a, (CategoricalIndex, Categorical)):
    categories = a.categories
    a = Categorical.from_codes(
        np.arange(len(categories)), categories=categories, ordered=a.ordered
    )
exit(a)
