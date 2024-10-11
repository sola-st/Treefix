# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
"""Reindex to a cartesian production for the groupers,
    preserving the nature (Categorical) of each grouper
    """

def f(a):
    if isinstance(a, (CategoricalIndex, Categorical)):
        categories = a.categories
        a = Categorical.from_codes(
            np.arange(len(categories)), categories=categories, ordered=a.ordered
        )
    exit(a)

index = MultiIndex.from_product(map(f, args), names=names)
exit(result.reindex(index, fill_value=fill_value).sort_index())
