# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("all_models_test")
abs_path = os.path.join(save_dir, "model-0")
for paths in [None, [], ["model-2"]]:
    ckpt = checkpoint_management.generate_checkpoint_state_proto(
        save_dir, abs_path, all_model_checkpoint_paths=paths)
    self.assertEqual(ckpt.model_checkpoint_path, abs_path)
    self.assertTrue(os.path.isabs(ckpt.model_checkpoint_path))
    self.assertEqual(
        len(ckpt.all_model_checkpoint_paths), len(paths) if paths else 1)
    self.assertEqual(ckpt.all_model_checkpoint_paths[-1], abs_path)
