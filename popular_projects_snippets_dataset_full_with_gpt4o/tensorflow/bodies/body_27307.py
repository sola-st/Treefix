# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
ds1 = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds2 = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
# iteration 1
self.assertDatasetProduces(ds1, list(range(num_elements)))
self.assertDatasetProduces(ds2, [])
# iteration 2
self.assertDatasetProduces(ds2, list(range(num_elements)))
self.assertDatasetProduces(ds1, [])
