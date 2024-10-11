# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dss = [dataset_ops.Dataset.range(10).map(map_fn) for _ in range(10)]
ds = dataset_ops.Dataset.from_tensor_slices(dss)
ds = ds.flat_map(lambda x: x)
self.assertDatasetProduces(
    ds, expected_output=[map_fn(x) for x in list(range(10)) * 10])
