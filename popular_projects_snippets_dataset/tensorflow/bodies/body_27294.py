# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
num_repetitions = 5
ds = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = ds.repeat(num_repetitions)
self.assertDatasetProduces(
    ds, expected_output=num_repetitions * list(range(num_elements)))
