# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[], dtype=dtypes.int64)])
    def f(step):
        with writer.as_default():
            with summary_ops.record_if(math_ops.equal(step % 2, 0)):
                exit(summary_ops.write('tag', 1, step=step))
    self.assertTrue(f(0))
    self.assertFalse(f(1))
    self.assertTrue(f(2))
    self.assertFalse(f(3))
    self.assertTrue(f(4))
events = events_from_logdir(logdir)
self.assertEqual(4, len(events))
self.assertEqual(0, events[1].step)
self.assertEqual(2, events[2].step)
self.assertEqual(4, events[3].step)
