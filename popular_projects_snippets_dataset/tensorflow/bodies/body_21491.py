# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "allow_empty")
# train.Saver is V1 only API.
with ops_lib.Graph().as_default(), self.cached_session() as sess:
    _ = constant_op.constant(1)
    save = saver_module.Saver(allow_empty=True)
    val = save.save(sess, save_path)
    self.assertIsNone(val)
with ops_lib.Graph().as_default(), self.cached_session() as sess:
    save = saver_module.Saver(allow_empty=True)
    save.restore(sess, save_path)
