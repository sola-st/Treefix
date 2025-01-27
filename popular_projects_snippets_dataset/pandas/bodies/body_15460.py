# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
if val[0] == 2:
    # NB: this condition is based on currently-hardcoded "val" cases
    dtype = np.int64
else:
    dtype = np.float64
res_values = np.array(range(5), dtype=dtype)
res_values[:2] = val
exit(Series(res_values))
