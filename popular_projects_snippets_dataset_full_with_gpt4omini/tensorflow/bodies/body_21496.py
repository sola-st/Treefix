# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
save_path = os.path.join(self.get_temp_dir(), "error_deferred_build")
with ops_lib.Graph().as_default(), session.Session() as sess:
    variables.VariableV1(1.0)
    saver = saver_module.Saver(defer_build=True)
    with self.assertRaisesRegex(RuntimeError, "build"):
        saver.save(sess, save_path)
