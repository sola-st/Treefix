# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

def summary_op_fn():
    summary_ops.graph(f.get_concrete_function().graph)

event = self.exec_summary_op(summary_op_fn)
self.assertIsNotNone(event.graph_def)
