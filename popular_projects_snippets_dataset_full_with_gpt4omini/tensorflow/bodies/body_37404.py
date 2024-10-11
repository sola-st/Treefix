# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    writer.close()
    writer.close()  # redundant close() is a no-op
    writer.flush()  # redundant flush() is a no-op
    with self.assertRaisesRegex(RuntimeError, 'already closed'):
        writer.init()
    with self.assertRaisesRegex(RuntimeError, 'already closed'):
        with writer.as_default():
            self.fail('should not get here')
    with self.assertRaisesRegex(RuntimeError, 'already closed'):
        writer.set_as_default()
