# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
# Two writers with the same logdir should not share state.
logdir = self.get_temp_dir()
with context.eager_mode():
    writer1 = summary_ops.create_file_writer_v2(logdir)
    with writer1.as_default():
        summary_ops.write('tag', 1, step=1)
    event_files = gfile.Glob(os.path.join(logdir, '*'))
    self.assertEqual(1, len(event_files))
    file1 = event_files[0]

    writer2 = summary_ops.create_file_writer_v2(logdir)
    with writer2.as_default():
        summary_ops.write('tag', 1, step=2)
    event_files = gfile.Glob(os.path.join(logdir, '*'))
    self.assertEqual(2, len(event_files))
    event_files.remove(file1)
    file2 = event_files[0]

    # Extra writes to ensure interleaved usage works.
    with writer1.as_default():
        summary_ops.write('tag', 1, step=1)
    with writer2.as_default():
        summary_ops.write('tag', 1, step=2)

events = iter(events_from_file(file1))
self.assertEqual('brain.Event:2', next(events).file_version)
self.assertEqual(1, next(events).step)
self.assertEqual(1, next(events).step)
self.assertRaises(StopIteration, lambda: next(events))
events = iter(events_from_file(file2))
self.assertEqual('brain.Event:2', next(events).file_version)
self.assertEqual(2, next(events).step)
self.assertEqual(2, next(events).step)
self.assertRaises(StopIteration, lambda: next(events))
