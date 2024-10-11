# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    handle = _eager_safe_var_handle_op(
        dtype=dtypes.int32, shape=[1], name="foo")
    resource_variable_ops.assign_variable_op(
        handle, constant_op.constant([1]))
    # The error message varies depending on whether it is being raised
    # by the kernel or shape inference. The shape inference code path can
    # be reached when running in eager op as function mode where each op
    # is wrapped in a tf.function.
    with self.assertRaisesRegex(
        errors.InvalidArgumentError, r"Trying to .* variable with wrong "
        r"dtype. Expected int32 got float"):
        resource_variable_ops.assign_variable_op(
            handle, constant_op.constant([1.], dtype=dtypes.float32))
