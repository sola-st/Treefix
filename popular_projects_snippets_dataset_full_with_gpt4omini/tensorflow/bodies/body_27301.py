# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset_id = data_service_ops.register_dataset(
    cluster.dispatcher.target,
    dataset_ops.Dataset.range(10),
    compression=self._get_compression())
with self.assertRaisesRegex(ValueError, "`job_name` must not be empty"):
    data_service_ops.from_dataset_id(
        dataset_id=dataset_id,
        processing_mode="parallel_epochs",
        service=cluster.dispatcher.target,
        job_name="")
