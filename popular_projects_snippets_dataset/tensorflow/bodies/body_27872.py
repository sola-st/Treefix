# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(40)
step_counter = variables.Variable(0, trainable=False)
checkpoint_args = {
    "checkpoint_interval": 5,
    "step_counter": step_counter,
    "directory": self._checkpoint_prefix,
    "max_to_keep": 10,
}
dataset.save(self._save_dir, checkpoint_args=checkpoint_args)
num_checkpoint_files = len(list(os.listdir(self._checkpoint_prefix)))
# We expect (2 * 8) + 1 files.
self.assertEqual(17, num_checkpoint_files)
