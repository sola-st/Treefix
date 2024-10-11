# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.graph_mode(), ops.Graph().as_default():
    writer = summary_ops.create_file_writer_v2(logdir)
    with self.cached_session() as sess:
        for _ in range(10):
            sess.run(writer.init())
            sess.run(writer.close())
event_files = gfile.Glob(os.path.join(logdir, '*'))
self.assertLen(event_files, 10)
