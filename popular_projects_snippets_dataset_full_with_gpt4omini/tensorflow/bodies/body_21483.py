# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
# train.Saver is V1 only API.
with ops_lib.Graph().as_default():
    v0 = variables.VariableV1(0, name="v0")
    filename = b"somerandomfilename"
    save = saver_module.Saver({"v0": v0}, filename=filename)
    with self.cached_session() as sess:
        tensor = sess.graph.get_tensor_by_name(
            save.saver_def.filename_tensor_name)
        self.assertEqual(self.evaluate(tensor), filename)
