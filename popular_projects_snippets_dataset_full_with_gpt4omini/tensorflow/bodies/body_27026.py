# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
io.save(dataset, self._test_dir)
with self.assertRaises(ValueError):
    _ = io.load(self._test_dir)
