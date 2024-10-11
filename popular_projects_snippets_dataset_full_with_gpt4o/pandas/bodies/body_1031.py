# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_indexing_slow.py
# GH7724, GH2646

with warnings.catch_warnings(record=True):
    if lexsort_depth == 0:
        df = frame.copy()
    else:
        df = frame.sort_values(by=cols[:lexsort_depth])

    mi = df.set_index(cols[:-1])
    assert not mi.index._lexsort_depth < lexsort_depth
    validate(mi, df, key)
