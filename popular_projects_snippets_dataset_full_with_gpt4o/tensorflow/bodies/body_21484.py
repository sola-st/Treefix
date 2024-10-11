# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
v0 = variables.VariableV1(0, name="v0")
for ver in (saver_pb2.SaverDef.V1, saver_pb2.SaverDef.V2):
    with self.cached_session() as sess:
        save = saver_module.Saver({"v0": v0}, write_version=ver)
        with self.assertRaisesRegex(
            ValueError, "The passed save_path is not a valid checkpoint:"):
            save.restore(sess, "invalid path")
