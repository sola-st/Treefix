# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
v = variables_lib.Variable(1.0)
ckpt = trackable_utils.Checkpoint(v=v)
self.evaluate(v.initializer)
prefix = pathlib.Path(self.get_temp_dir()) / "ckpt"
with ops.default_session(None):
    with self.assertRaisesRegex(RuntimeError, "create a session"):
        ckpt.write(prefix)
