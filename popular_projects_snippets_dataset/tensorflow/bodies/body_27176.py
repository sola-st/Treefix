# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=1,
    num_remote_workers=3,
    worker_addresses=["localhost:%port%"] * 5,
    worker_tags=[_COLOCATED_WORKER_TAG])
cluster.start_remote_worker(worker_tags=None)

num_elements = 100
dataset = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.FILE_OR_DATA)

# Static sharding will only read from the local worker.
self.assertDatasetProduces(dataset, list(range(0, num_elements, 5)))
