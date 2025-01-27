# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster_1 = data_service_test_base.TestCluster(num_workers=1)
cluster_2 = data_service_test_base.TestCluster(num_workers=1)
num_sizes = 10
size_repeats = 5
numbers = [1 * i for i in range(num_sizes)] * size_repeats
ds = dataset_ops.Dataset.from_tensor_slices(numbers)
ds = self.make_distributed_dataset(
    ds, cluster_1, processing_mode=data_service_ops.ShardingPolicy.OFF)
ds = ds.map(lambda x: x + 1)
ds = self._make_dynamic_sharding_dataset(ds, cluster_2)

error_regex = ("Cannot create split providers for dataset " +
               "of type DataServiceDataset")
with self.assertRaisesRegex(errors.UnimplementedError, error_regex):
    self.getDatasetOutput(ds)
