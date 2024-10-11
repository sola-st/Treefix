# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(), "no_checkpoints_found")

num_found = 0
for _ in checkpoint_utils.checkpoints_iterator(checkpoint_dir, timeout=0):
    num_found += 1
self.assertEqual(num_found, 0)
