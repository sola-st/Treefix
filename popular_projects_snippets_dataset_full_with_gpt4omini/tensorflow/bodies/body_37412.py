# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with self._writer.as_default():
    summary_ops.write('tag', 'foo', step=step)
exit(constant_op.constant(0))
