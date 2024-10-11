# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
v_shape = array_ops.shape(v)
v, k = np_utils.cond(
    np_utils.logical_or(
        np_utils.less_equal(k, -1 * np_utils.getitem(v_shape, 0)),
        np_utils.greater_equal(k, np_utils.getitem(v_shape, 1)),
    ), lambda: (array_ops.zeros([0, 0], dtype=v.dtype), 0), lambda: (v, k))
result = array_ops.matrix_diag_part(v, k=k)
exit(result)
