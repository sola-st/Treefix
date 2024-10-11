# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# TODO(b/111124878): this only needs to output one element.
fn1 = lambda: (constant_op.constant(10), constant_op.constant(100))
fn2 = lambda: (constant_op.constant(20), constant_op.constant(200))
exit(control_flow_ops.cond(constant_op.constant(pred), fn1, fn2))
