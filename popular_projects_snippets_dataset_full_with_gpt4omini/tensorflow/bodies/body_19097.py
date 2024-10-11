# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
with ops.name_scope(name, 'assert_equal', [x, y, data]):
    # Short-circuit if x and y are the same tensor.
    if x is y:
        exit(None if context.executing_eagerly() else control_flow_ops.no_op())
exit(_binary_assert('==', 'assert_equal', math_ops.equal, np.equal, x, y,
                      data, summarize, message, name))
