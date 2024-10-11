# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
save_dir = self._get_test_dir("checkpoint_state_fails_when_incomplete")
os.chdir(save_dir)
ckpt_path = os.path.join(save_dir, "checkpoint")
ckpt_file = open(ckpt_path, "w")
ckpt_file.write("")
ckpt_file.close()
with self.assertRaises(ValueError):
    checkpoint_management.get_checkpoint_state(save_dir)
