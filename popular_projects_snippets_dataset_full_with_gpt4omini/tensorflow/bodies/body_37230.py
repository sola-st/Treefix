# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

@function.Defun(dtypes.float32)
def func(x):
    exit(math_ops.square(math_ops.square(x)))

with self.cached_session():
    x = constant_op.constant(2.0, dtypes.float32)
    r = control_flow_ops.while_loop(
        lambda i, v: i < 2, lambda i, v: [i + 1, func(v)],
        [constant_op.constant(0), x],
        [tensor_shape.unknown_shape(),
         tensor_shape.unknown_shape()])
    grad = gradients_impl.gradients(r, x)[0]
    self.assertEqual(self.evaluate(r[1]), 65536.0)
    self.assertEqual(self.evaluate(grad), 524288.0)
    # while_v2 does not have stacks.
    if not control_flow_util.ENABLE_CONTROL_FLOW_V2:
        self.assertEqual(
            len([op for op in x.graph.get_operations() if op.type == "StackV2"
                ]), 1)
