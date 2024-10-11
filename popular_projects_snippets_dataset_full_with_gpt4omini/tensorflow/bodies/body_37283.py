# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    x = constant_op.constant(1)
    y = constant_op.constant(2)
    z = constant_op.constant(3)
    f1 = lambda: constant_op.constant(17)
    f2 = lambda: constant_op.constant(23)
    f3 = lambda: constant_op.constant(-1)

    r1 = control_flow_ops.case(
        [(x < y, f1), (x > z, f2)], default=f3, exclusive=True)
    self.assertAllEqual(r1.numpy(), 17)
