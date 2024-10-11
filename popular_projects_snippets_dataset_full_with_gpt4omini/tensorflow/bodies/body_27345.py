# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = self.make_distributed_range_dataset(
    num_elements=10,
    cluster=cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = self.make_distributed_dataset(
    dataset=ds,
    cluster=cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(ds, list(range(10)))
