# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset_id = "UnregisteredID"
element_spec = tensor_spec.TensorSpec(shape=(), dtype=dtypes.variant)
with self.assertRaisesRegex(errors.NotFoundError,
                            f"Dataset id {dataset_id} not found."):
    from_dataset_id_ds = data_service_ops.from_dataset_id(
        data_service_ops.ShardingPolicy.OFF,
        cluster.dispatcher.target,
        dataset_id,
        element_spec,
        data_transfer_protocol=self._get_data_transfer_protocol())
    self.evaluate(self.getNext(from_dataset_id_ds)())
