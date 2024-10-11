# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        with ops.device('/GPU:0'):
            value = constant_op.constant(42.0)
            step = constant_op.constant(12, dtype=dtypes.int64)
            summary_ops.write('tag', value, step=step).numpy()
empty_metadata = summary_pb2.SummaryMetadata()
events = events_from_logdir(logdir)
self.assertEqual(2, len(events))
self.assertEqual(12, events[1].step)
self.assertEqual(42, to_numpy(events[1].summary.value[0]))
self.assertEqual(empty_metadata, events[1].summary.value[0].metadata)
