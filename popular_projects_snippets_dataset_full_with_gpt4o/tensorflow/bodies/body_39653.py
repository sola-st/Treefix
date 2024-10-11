# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
v = variables_lib.Variable([1.0, 1.0])
w = variables_lib.Variable([1.0])
ckpt = trackable_utils.Checkpoint(v=v)
save_path = ckpt.save(os.path.join(self.get_temp_dir(), "ckpt"))

with self.assertRaisesRegex(ValueError, "incompatible tensor with shape"):
    trackable_utils.Checkpoint(v=w).restore(save_path)
