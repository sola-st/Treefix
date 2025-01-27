# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.from_tensor_slices([1, 5, 3, 2, 8])
ds = ds.map(math_ops.range)
ds = ds.apply(batching.dense_to_ragged_batch(2))
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
results = [elem.to_tensor() for elem in ds]
self.assertAllEqual(results[0], [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4]])
self.assertAllEqual(results[1], [[0, 1, 2], [0, 1, 0]])
self.assertAllEqual(results[2], [[0, 1, 2, 3, 4, 5, 6, 7]])
