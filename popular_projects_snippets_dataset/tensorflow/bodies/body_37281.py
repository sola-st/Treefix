# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    t1 = constant_op.constant(1)
    t2 = constant_op.constant(2)
    t3 = control_flow_ops.with_dependencies(t1, t2)
    self.assertAllEqual(t2.numpy(), t3.numpy())
