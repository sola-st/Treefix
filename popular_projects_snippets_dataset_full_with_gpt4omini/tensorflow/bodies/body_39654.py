# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
v = variables_lib.Variable(1.0)
w = variables_lib.Variable(0.0)
ckpt = trackable_utils.Checkpoint(v=v)
prefix = pathlib.Path(self.get_temp_dir()) / "ckpt"
save_path = ckpt.save(prefix)
save_path = pathlib.Path(save_path)
ckpt2 = trackable_utils.Checkpoint(v=w)
ckpt2.restore(save_path)
self.assertEqual(ckpt.v.numpy(), 1.0)
