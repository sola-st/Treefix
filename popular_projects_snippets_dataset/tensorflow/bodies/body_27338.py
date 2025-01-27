# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
ds_1 = dataset_ops.Dataset.range(10)
ds_2 = dataset_ops.Dataset.range(10)
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
id_1 = data_service_ops.register_dataset(
    cluster.dispatcher_address(), ds_1, compression=self._get_compression())
id_2 = data_service_ops.register_dataset(
    cluster.dispatcher_address(), ds_2, compression=self._get_compression())
self.assertEqual(self.evaluate(id_1), self.evaluate(id_2))
