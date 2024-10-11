# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=1,
    num_remote_workers=3,
    worker_tags=[_COLOCATED_WORKER_TAG, "COLOCATED_2", "COLOCATED_3"])
num_elements = 100
dataset = self.make_distributed_range_dataset(num_elements, cluster)
# Only reads from the local worker.
self.assertDatasetProduces(dataset, list(range(num_elements)))
