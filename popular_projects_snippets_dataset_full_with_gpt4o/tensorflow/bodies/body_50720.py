# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer_test.py
# Test case for GitHub issue 46909
logdir = self.get_temp_dir()
with session.Session() as sess:
    with self.assertRaises(errors_impl.InvalidArgumentError):
        writer = summary_ops_v2.create_file_writer(
            logdir=logdir, flush_millis=[1, 2])
        sess.run(writer.init())
        sess.run(writer.flush())
