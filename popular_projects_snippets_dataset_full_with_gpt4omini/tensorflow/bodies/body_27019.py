# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
io.save(dataset, self._test_dir, compression=compression)
dataset2 = io.load(
    self._test_dir, dataset.element_spec, compression=compression)
self.assertDatasetProduces(dataset2, range(42))
