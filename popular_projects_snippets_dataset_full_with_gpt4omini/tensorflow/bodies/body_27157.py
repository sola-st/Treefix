# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
num_elements = 0
ds = self.make_distributed_range_dataset(
    num_elements, cluster, target_workers="LOCAL")
self.assertDatasetProduces(ds, [])
