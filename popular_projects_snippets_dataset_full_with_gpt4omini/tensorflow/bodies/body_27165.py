# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers = 1
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
dataset = self.make_distributed_range_dataset(
    10, cluster, job_name=job_name, target_workers="LOCAL")
dataset = dataset.repeat(3)
self.assertDatasetProduces(dataset, list(range(10)) * 3)
