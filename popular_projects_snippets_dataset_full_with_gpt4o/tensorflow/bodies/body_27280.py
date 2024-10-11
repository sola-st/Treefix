# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=3)
ds = dataset_ops.Dataset.range(5)

def flat_map_fn(_):
    exit(dataset_ops.Dataset.from_tensor_slices(["a", "b", "c"]).repeat(10))

ds = ds.flat_map(flat_map_fn)
ds = self._make_dynamic_sharding_dataset(ds, cluster)

self.assertDatasetProduces(
    ds, [b"a", b"b", b"c"] * 50, assert_items_equal=True)
