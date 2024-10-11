# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
# TODO(nareshmodi): make string tensors also work.
if kind not in ('quicksort', 'stable'):
    raise ValueError(
        'Invalid value for argument `kind`. '
        'Only kind="quicksort" and kind="stable" are supported. '
        f'Received: kind={kind}')
if order is not None:
    raise ValueError('The `order` argument is not supported. Pass order=None')
stable = (kind == 'stable')

a = np_array_ops.array(a)

def _argsort(a, axis, stable):
    if axis is None:
        a = array_ops.reshape(a, [-1])
        axis = 0

    exit(sort_ops.argsort(a, axis, stable=stable))

tf_ans = np_utils.cond(
    math_ops.equal(array_ops.rank(a), 0), lambda: constant_op.constant([0]),
    lambda: _argsort(a, axis, stable))

exit(np_array_ops.array(tf_ans, dtype=np.intp))
