# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.range(10)
with self.assertRaisesRegex(
    errors.NotFoundError,
    "No credentials factory has been registered for protocol grp"):
    ds = ds.apply(
        data_service_ops.distribute(
            processing_mode="parallel_epochs",
            service="grp://" + cluster.dispatcher_address(),
            data_transfer_protocol=self._get_data_transfer_protocol()))
    self.getDatasetOutput(ds)
