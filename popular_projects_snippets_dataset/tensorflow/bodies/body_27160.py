# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=3, num_remote_workers=3)
ds = dataset_ops.Dataset.range(10)
datasets = [
    self.make_distributed_dataset(
        ds, cluster, job_name="test_job", target_workers=target_workers)
    for target_workers in ["AUTO", "ANY", "LOCAL"]
]

with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "but found an existing job with different parameters: "
    "Existing target workers: <AUTO>"):
    for dataset in datasets:
        self.getDatasetOutput(dataset)
