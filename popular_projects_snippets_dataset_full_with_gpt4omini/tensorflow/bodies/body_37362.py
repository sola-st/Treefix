# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
pb1 = summary_pb2.Summary()
pb1.value.add().simple_value = 1.0
pb1.value.add().simple_value = 2.0
pb2 = summary_pb2.Summary()
pb2.value.add().simple_value = 3.0
pb3 = summary_pb2.Summary()
pb3.value.add().simple_value = 4.0
pb3.value.add().simple_value = 5.0
pb3.value.add().simple_value = 6.0
pbs = [pb.SerializeToString() for pb in (pb1, pb2, pb3)]
with context.eager_mode():
    with summary_ops.create_file_writer_v2(logdir).as_default():
        output = summary_ops.write_raw_pb(pbs, step=12)
        self.assertTrue(output.numpy())
events = events_from_logdir(logdir)
self.assertEqual(2, len(events))
self.assertEqual(12, events[1].step)
expected_pb = summary_pb2.Summary()
for i in range(6):
    expected_pb.value.add().simple_value = i + 1.0
self.assertProtoEquals(expected_pb, events[1].summary)
