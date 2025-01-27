# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
with self.assertRaisesRegex(ValueError, 'Must enable trace before export.'):
    summary_ops.trace_export(name='foo', step=1)
