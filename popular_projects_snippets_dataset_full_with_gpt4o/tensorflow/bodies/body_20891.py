# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = pathlib.Path(self.get_temp_dir()) / "one_checkpoint_found"
if not gfile.Exists(checkpoint_dir):
    gfile.MakeDirs(checkpoint_dir)

save_path = checkpoint_dir / "model.ckpt"

a = resource_variable_ops.ResourceVariable(5)
self.evaluate(a.initializer)
checkpoint = trackable_utils.Checkpoint(a=a)
checkpoint.save(file_prefix=save_path)

num_found = 0
for _ in checkpoint_utils.checkpoints_iterator(checkpoint_dir, timeout=0):
    num_found += 1
self.assertEqual(num_found, 1)
