# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
other = idx.to_flat_index().astype("category")
res_names = [None] * idx.nlevels

result = getattr(idx, method)(other, sort=sort)
expected = getattr(idx, method)(idx, sort=sort).rename(res_names)
tm.assert_index_equal(result, expected)

result = getattr(idx, method)(other[:5], sort=sort)
expected = getattr(idx, method)(idx[:5], sort=sort).rename(res_names)
tm.assert_index_equal(result, expected)
