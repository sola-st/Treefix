# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
num_workers = 3
cluster = data_service_test_base.TestCluster(
    num_workers=num_workers,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
ds = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    max_outstanding_requests=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(
    ds, num_workers * list(range(num_elements)), assert_items_equal=True)
