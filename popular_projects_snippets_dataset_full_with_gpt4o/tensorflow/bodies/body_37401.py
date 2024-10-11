# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with context.eager_mode():
    with self.assertRaisesRegex(ValueError, 'Invalid argument to flush'):
        summary_ops.flush(writer=())
