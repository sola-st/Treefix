# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers,
    worker_tags=[_COLOCATED_WORKER_TAG])
num_consumers = 4
dataset = self.make_coordinated_read_dataset(cluster, num_consumers)
get_next = self.getNext(dataset, requires_initialization=True)
results = [self.evaluate(get_next()) for _ in range(200)]
self.checkCoordinatedReadGroups(results, num_consumers)
