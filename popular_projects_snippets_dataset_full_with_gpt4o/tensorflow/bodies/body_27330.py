# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 100
ds1 = dataset_ops.Dataset.range(num_elements)
ds1 = self.make_distributed_dataset(
    ds1,
    cluster,
    processing_mode="distributed_epoch",
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds2 = dataset_ops.Dataset.range(num_elements)
ds2 = self.make_distributed_dataset(
    ds2,
    cluster,
    processing_mode="parallel_epochs",
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.zip((ds1, ds2))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "but found an existing job with diff"):
    self.getDatasetOutput(ds)
