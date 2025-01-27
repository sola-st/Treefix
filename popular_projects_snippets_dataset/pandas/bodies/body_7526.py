# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
# TODO: more informative test name
# GH5873
for a in [101, 102]:
    mi = MultiIndex.from_arrays([[101, a], [3.5, np.nan]])
    assert not mi.has_duplicates

    tm.assert_numpy_array_equal(mi.duplicated(), np.zeros(2, dtype="bool"))

for n in range(1, 6):  # 1st level shape
    for m in range(1, 5):  # 2nd level shape
        # all possible unique combinations, including nan
        codes = product(range(-1, n), range(-1, m))
        mi = MultiIndex(
            levels=[list("abcde")[:n], list("WXYZ")[:m]],
            codes=np.random.permutation(list(codes)).T,
        )
        assert len(mi) == (n + 1) * (m + 1)
        assert not mi.has_duplicates

        tm.assert_numpy_array_equal(
            mi.duplicated(), np.zeros(len(mi), dtype="bool")
        )
