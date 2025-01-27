# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
checkpoint_args = {
    "directory": self._checkpoint_prefix,
    "incorrect_arg": "incorrect_arg"
}
with self.assertRaises(TypeError):
    dataset.save(
        dataset, self._save_dir, checkpoint_args=checkpoint_args)
