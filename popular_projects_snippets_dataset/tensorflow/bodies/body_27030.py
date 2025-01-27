# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(40)
checkpoint_args = {"directory": self._checkpoint_prefix, "max_to_keep": 50}
io.save(dataset, self._save_dir, checkpoint_args=checkpoint_args)
num_checkpoint_files = len(list(os.listdir(self._checkpoint_prefix)))
# By default, we checkpoint every increment. Each checkpoint writes a
# file containing the data and a file containing the index. There is
# also an overall checkpoint file. Thus, we expect (2 * 40) + 1 files.
self.assertEqual(81, num_checkpoint_files)
