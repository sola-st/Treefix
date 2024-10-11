# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    t = constant_op.constant([[1, 2], [3, 4]])
    with summary_ops.create_file_writer_v2(logdir).as_default():
        summary_ops.write('tag', t, step=12)
    expected = t.numpy()
events = events_from_logdir(logdir)
value = events[1].summary.value[0]
self.assertAllEqual(expected, to_numpy(value))
