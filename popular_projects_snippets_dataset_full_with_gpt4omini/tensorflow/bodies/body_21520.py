# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
checkpoint_state = checkpoint_management.get_checkpoint_state(save_dir)
self.assertEqual(checkpoint_state.model_checkpoint_path,
                 model_checkpoint_path)
self.assertEqual(checkpoint_state.all_model_checkpoint_paths,
                 all_model_checkpoint_paths)
