# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("fspath")
os.chdir(save_dir)
# Make a temporary train directory.
train_dir = "train"
os.mkdir(train_dir)
abs_path = os.path.join(save_dir, "model-0")
rel_path = os.path.join("train", "model-2")
checkpoint_management.update_checkpoint_state(
    train_dir, rel_path, all_model_checkpoint_paths=[abs_path, rel_path])
ckpt = checkpoint_management.get_checkpoint_state(pathlib.Path(train_dir))
self.assertEqual(ckpt.model_checkpoint_path, rel_path)
