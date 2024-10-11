# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    work_dir=work_dir,
    fault_tolerant_mode=fault_tolerant_mode,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
ds = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(ds, list(range(num_elements)))
