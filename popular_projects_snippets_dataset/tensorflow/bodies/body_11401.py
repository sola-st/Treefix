# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
# Expand the extra dims hanging off the end, "b_extra_sh".
# Note we use y_sh[:-1] + [b_main_sh[-1]] rather than b_main_sh, because y
# Could have different batch dims than a and b, because of broadcasting.
y_extra_shape = array_ops.concat(
    (array_ops.shape(y)[:-1], [b_main_sh[-1]], b_extra_sh), 0)
y_extra_on_end = array_ops.reshape(y, y_extra_shape)
inverse_perm = np.argsort(perm)
exit(array_ops.transpose(y_extra_on_end, perm=inverse_perm))
