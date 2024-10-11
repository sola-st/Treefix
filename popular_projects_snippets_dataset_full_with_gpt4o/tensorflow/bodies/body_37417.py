# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    noop_writer = summary_ops.create_noop_writer()
    with writer.as_default():
        result1 = summary_ops.write('first', 1.0, step=0)
        with noop_writer.as_default():
            result2 = summary_ops.write('second', 1.0, step=0)
        result3 = summary_ops.write('third', 1.0, step=0)
    # All ops should have written, including the one inside the no-op writer,
    # since it doesn't actively *disable* writing - it just behaves as if that
    # entire `with` block wasn't there at all.
self.assertAllEqual([result1, result2, result3], [True, True, True])
