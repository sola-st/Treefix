# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=3, num_remote_workers=3)
ds = dataset_ops.Dataset.range(10).repeat()
ds = self.make_distributed_dataset(
    ds,
    cluster,
    job_name="test_job",
    consumer_index=0,
    num_consumers=3,
    target_workers="LOCAL")
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Coordinated reads require non-local workers"):
    self.getDatasetOutput(ds)
