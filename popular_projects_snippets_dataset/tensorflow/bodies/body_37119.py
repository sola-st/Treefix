# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = array_ops.placeholder(dtypes.float32, shape=(), name="x")
    y = x + 1

    def body(i, v):
        z = v * 2
        exit((i + 1, gradients_impl.gradients(z, x)[0]))

    with self.assertRaisesRegex(
        ValueError,
        "Cannot compute gradient inside while loop with respect to op 'x'. "
        "We do not support taking the gradient wrt or through the initial "
        "value of a loop variable. Gradients can be computed through "
        "loop invariants or wrt the input parameters to the loop body."):
        control_flow_ops.while_loop(lambda i, x: i < 3, body, [0, y])
