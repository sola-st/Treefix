# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer_test.py
"""Function that asserts it's gradient has a certain value."""
x = array_ops.identity(x)
def grad(dx):
    """Gradient function that asserts the gradient has a certain value."""
    if expected_dtype:
        assert dx.dtype == expected_dtype, (
            'dx.dtype should be %s but is: %s' % (expected_dtype, dx.dtype))
    expected_tensor = ops.convert_to_tensor_v2(
        expected_gradient, dtype=dx.dtype, name='expected_gradient')
    # Control dependency is to ensure input is available. It's possible the
    # dataset will throw a StopIteration to indicate there is no more data, in
    # which case we don't want to run the assertion.
    with ops.control_dependencies([x]):
        assert_op = check_ops.assert_equal(dx, expected_tensor)
    with ops.control_dependencies([assert_op]):
        dx = array_ops.identity(dx)
    exit(dx)
exit((x, grad))
