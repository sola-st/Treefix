# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
ds = dataset_ops.Dataset.range(num_elements)
ds = self.make_distributed_dataset(
    ds, cluster, job_name="test", consumer_index=0, num_consumers=1)

with self.assertRaisesRegex(
    errors.FailedPreconditionError, "Encountered end of sequence on a "
    "round-robin read iterator"):
    self.getDatasetOutput(ds)
