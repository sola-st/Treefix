# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("checkpoint_completes_relative_paths")
os.chdir(save_dir)
ckpt_path = os.path.join(save_dir, "checkpoint")
ckpt_file = open(ckpt_path, "w")
ckpt_file.write("""
        model_checkpoint_path: "./model.ckpt-687529"
        all_model_checkpoint_paths: "./model.ckpt-687500"
        all_model_checkpoint_paths: "./model.ckpt-687529"
        """)
ckpt_file.close()
ckpt = checkpoint_management.get_checkpoint_state(save_dir)
self.assertEqual(ckpt.model_checkpoint_path,
                 os.path.join(save_dir, "./model.ckpt-687529"))
self.assertEqual(ckpt.all_model_checkpoint_paths[0],
                 os.path.join(save_dir, "./model.ckpt-687500"))
self.assertEqual(ckpt.all_model_checkpoint_paths[1],
                 os.path.join(save_dir, "./model.ckpt-687529"))
