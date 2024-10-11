# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("update_checkpoint_state")
os.chdir(save_dir)
abs_path2 = os.path.join(save_dir, "model-2")
rel_path2 = "model-2"
abs_path0 = os.path.join(save_dir, "model-0")
rel_path0 = "model-0"
checkpoint_management.update_checkpoint_state_internal(
    save_dir=save_dir,
    model_checkpoint_path=abs_path2,
    all_model_checkpoint_paths=[rel_path0, abs_path2],
    save_relative_paths=True)

# File should contain relative paths.
file_content = file_io.read_file_to_string(
    os.path.join(save_dir, "checkpoint"))
ckpt = CheckpointState()
text_format.Merge(file_content, ckpt)
self.assertEqual(ckpt.model_checkpoint_path, rel_path2)
self.assertEqual(len(ckpt.all_model_checkpoint_paths), 2)
self.assertEqual(ckpt.all_model_checkpoint_paths[-1], rel_path2)
self.assertEqual(ckpt.all_model_checkpoint_paths[0], rel_path0)

# get_checkpoint_state should return absolute paths.
ckpt = checkpoint_management.get_checkpoint_state(save_dir)
self.assertEqual(ckpt.model_checkpoint_path, abs_path2)
self.assertEqual(len(ckpt.all_model_checkpoint_paths), 2)
self.assertEqual(ckpt.all_model_checkpoint_paths[-1], abs_path2)
self.assertEqual(ckpt.all_model_checkpoint_paths[0], abs_path0)
