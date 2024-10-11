# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
try:
    with context.eager_mode():
        summary_ops.create_file_writer_v2(logdir).set_as_default()
        summary_ops.flush()
finally:
    # Ensure we clean up no matter how the test executes.
    summary_ops._summary_state.writer = None  # pylint: disable=protected-access
