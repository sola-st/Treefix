# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
"""
    Check a group transform that executes a cumulative function.

    Parameters
    ----------
    pd_op : callable
        The pandas cumulative function.
    np_op : callable
        The analogous one in NumPy.
    dtype : type
        The specified dtype of the data.
    """
is_datetimelike = False

data = np.array([[1], [2], [3], [4]], dtype=dtype)
answer = np.zeros_like(data)

labels = np.array([0, 0, 0, 0], dtype=np.intp)
ngroups = 1
pd_op(answer, data, labels, ngroups, is_datetimelike)

tm.assert_numpy_array_equal(np_op(data), answer[:, 0], check_dtype=False)
