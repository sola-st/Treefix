# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Regression test for lowering predicate from non-first output of an op."""

@eager_def_function.function
def foo():
    exit((constant_op.constant("foo"), constant_op.constant(True)))

r = control_flow_ops.cond(foo()[1], lambda: 1.0, lambda: 2.0)
self.assertEqual(self.evaluate(r), 1.0)
