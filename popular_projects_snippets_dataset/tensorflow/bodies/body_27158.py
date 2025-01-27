# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
"""This test ensures the remote workers are running and producing data."""

cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
num_elements = 10
ds = self.make_distributed_range_dataset(num_elements, cluster)
num_workers = num_local_workers + num_remote_workers
self.assertDatasetProduces(
    ds, num_workers * list(range(num_elements)), assert_items_equal=True)
