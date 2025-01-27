# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
ds = dataset_ops.Dataset.range(10)
ds = ds.apply(
    testing.assert_next(["Interleave", "Map", "Batch", "FiniteTake"]))
ds = ds.interleave(
    dataset_ops.Dataset.from_tensors,
    cycle_length=10,
    num_parallel_calls=10)
ds = ds.map(lambda x: x * x, num_parallel_calls=10)
ds = ds.batch(batch_size=5, num_parallel_calls=2)
ds = ds.prefetch(buffer_size=2)
ds = ds.take(2)
self.assertDatasetProduces(ds, [[0, 1, 4, 9, 16], [25, 36, 49, 64, 81]])
