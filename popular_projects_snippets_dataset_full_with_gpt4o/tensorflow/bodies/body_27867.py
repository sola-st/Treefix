# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
dataset.save(self._test_dir)
with self.assertRaises(ValueError):
    _ = dataset_ops.Dataset.load(self._test_dir)
