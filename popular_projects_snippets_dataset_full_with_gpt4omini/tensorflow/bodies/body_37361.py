# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
pb = summary_pb2.Summary()
pb.value.add().simple_value = 42.0
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    @def_function.function
    def f():
        with writer.as_default():
            exit(summary_ops.write_raw_pb(pb.SerializeToString(), step=12))
    output = f()
    self.assertTrue(output.numpy())
events = events_from_logdir(logdir)
self.assertEqual(2, len(events))
self.assertEqual(12, events[1].step)
self.assertProtoEquals(pb, events[1].summary)
