# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("abs_paths")
abs_path = os.path.join(save_dir, "model-0")
ckpt = checkpoint_management.generate_checkpoint_state_proto(
    save_dir, abs_path)
self.assertEqual(ckpt.model_checkpoint_path, abs_path)
self.assertTrue(os.path.isabs(ckpt.model_checkpoint_path))
self.assertEqual(len(ckpt.all_model_checkpoint_paths), 1)
self.assertEqual(ckpt.all_model_checkpoint_paths[-1], abs_path)
