# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
element = sparse_tensor.SparseTensor(
    indices=[[0]],
    values=constant_op.constant([0], dtype=dtypes.int32),
    dense_shape=[1])
ds = dataset_ops.Dataset.from_tensors(element)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
results = [sparse_ops.sparse_tensor_to_dense(elem) for elem in ds]
self.assertAllEqual(results, [[0]])
