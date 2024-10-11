# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
# see gh-4095
dtype = np.dtype(np_dtype).type
pd_op, np_op = group_cumsum, np.cumsum
_check_cython_group_transform_cumulative(pd_op, np_op, dtype)
