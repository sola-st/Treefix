# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
dataset = dataset_ops.Dataset.range(42)
@def_function.function
def save_fn():
    dataset.save(self._test_dir, compression=compression)
save_fn()
dataset = dataset_ops.Dataset.load(
    self._test_dir, dataset.element_spec, compression=compression)
self.assertDatasetProduces(dataset, range(42))
