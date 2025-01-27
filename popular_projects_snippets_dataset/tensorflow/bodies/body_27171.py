# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/multi_process_cluster_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
num_elements = 10
num_workers = num_local_workers + num_remote_workers
if num_workers == 0:
    exit()
dataset = self.make_distributed_range_dataset(num_elements, cluster)
self.assertDatasetProduces(
    dataset,
    num_workers * list(range(num_elements)),
    assert_items_equal=True)
