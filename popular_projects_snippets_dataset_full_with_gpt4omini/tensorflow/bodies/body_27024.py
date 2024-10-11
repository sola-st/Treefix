# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/io_test.py

dataset = dataset_ops.Dataset.range(42)

@def_function.function
def save_fn():
    io.save(dataset, self._test_dir, compression=compression)

save_fn()
dataset = io.load(
    self._test_dir, dataset.element_spec, compression=compression)
self.assertDatasetProduces(dataset, range(42))
