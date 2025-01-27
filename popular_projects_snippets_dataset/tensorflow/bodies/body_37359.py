# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
pb = summary_pb2.Summary()
pb.value.add().simple_value = 42.0
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        output = summary_ops.write_raw_pb(pb.SerializeToString(), step=12)
        self.assertTrue(output.numpy())
events = events_from_logdir(logdir)
self.assertEqual(2, len(events))
self.assertEqual(12, events[1].step)
self.assertProtoEquals(pb, events[1].summary)
