# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# RangeIndex is preserved by factorize, so preserved in levels
rng = Index(range(5))
other = ["a", "b"]
mi = MultiIndex.from_product([rng, other])
tm.assert_index_equal(mi._levels[0], rng, exact=True)
