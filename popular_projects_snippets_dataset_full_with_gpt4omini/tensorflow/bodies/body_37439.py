# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
x = constant_op.constant(2)
y = constant_op.constant(3)
summary_ops.trace_export(name='foo', step=1)
exit(x**y)
