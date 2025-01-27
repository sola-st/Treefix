# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py

@def_function.function
def f():
    x = constant_op.constant(2)
    y = constant_op.constant(3)
    exit(x**y)

try:
    summary_ops.set_step(42)
    event = self.run_trace(f, step=None)
    self.assertEqual(42, event.step)
finally:
    # Reset to default state for other tests.
    summary_ops.set_step(None)
