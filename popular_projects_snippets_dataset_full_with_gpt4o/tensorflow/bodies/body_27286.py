# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
with self.assertRaisesRegex(ValueError, "Invalid `compression` argument"):
    self.make_distributed_range_dataset(
        10,
        cluster,
        data_transfer_protocol=self._get_data_transfer_protocol(),
        compression="foo")
