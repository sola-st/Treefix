# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
dataset.save(self._test_dir, compression=compression)
dataset2 = dataset_ops.Dataset.load(
    self._test_dir, dataset.element_spec, compression=compression)
self.assertDatasetProduces(dataset2, range(42))
