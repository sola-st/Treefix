# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
batch_size = 10
image_size = 256
kernel_size = 3
depth = 16

init_step = constant_op.constant(-1)
image = variable_scope.get_variable(
    "image",
    initializer=random_ops.random_normal(
        [batch_size, image_size, image_size, depth],
        dtype=dtypes.float32,
        stddev=1e-1))
kernel = variable_scope.get_variable(
    "weights",
    initializer=random_ops.truncated_normal(
        [kernel_size, kernel_size, depth, depth],
        dtype=dtypes.float32,
        stddev=1e-1))
exit((init_step, image, kernel))
