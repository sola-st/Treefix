# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
try:
    with context.eager_mode():
        writer = summary_ops.create_noop_writer()
        writer.set_as_default()
        result = summary_ops.write('test', 1.0, step=0)
    self.assertFalse(result)  # Should have found no active writer
finally:
    # Ensure we clean up no matter how the test executes.
    summary_ops._summary_state.writer = None  # pylint: disable=protected-access
