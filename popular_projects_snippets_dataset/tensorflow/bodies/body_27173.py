# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers,
    worker_tags=[_COLOCATED_WORKER_TAG])
cluster.start_remote_worker(worker_tags=None)

num_elements = 100
dataset = self.make_distributed_range_dataset(num_elements, cluster)
# Reads from the local worker or non-colocated worker.
self.assertDatasetProduces(
    dataset, (num_local_workers + 1) * list(range(num_elements)),
    assert_items_equal=True)
