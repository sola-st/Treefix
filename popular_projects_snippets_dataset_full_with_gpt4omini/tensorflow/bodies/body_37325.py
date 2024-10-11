# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
metadata = summary_pb2.SummaryMetadata()
metadata.plugin_data.plugin_name = 'foo'
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        summary_ops.write('obj', 0, 0, metadata=metadata)
        summary_ops.write('bytes', 0, 0, metadata=metadata.SerializeToString())
        m = constant_op.constant(metadata.SerializeToString())
        summary_ops.write('string_tensor', 0, 0, metadata=m)
events = events_from_logdir(logdir)
self.assertEqual(4, len(events))
self.assertEqual(metadata, events[1].summary.value[0].metadata)
self.assertEqual(metadata, events[2].summary.value[0].metadata)
self.assertEqual(metadata, events[3].summary.value[0].metadata)
