# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers,
    worker_tags=[_COLOCATED_WORKER_TAG])

# num_elements needs to be bigger than (100 + <cpu core count>), the extra
# 100 is just a bit of margin. The CPU core count is involved as
# elements are prefetched, one element per CPU core.
num_elements = 200 + multiprocessing.cpu_count()
dataset = self.make_distributed_range_dataset(num_elements, cluster)
get_next = self.getNext(dataset)
results = [self.evaluate(get_next()) for _ in range(100)]

# Will only read from the two non-TPU workers.
cluster.start_remote_worker(worker_tags=None)
cluster.start_remote_worker(worker_tags=[_COLOCATED_WORKER_TAG])
cluster.start_remote_worker(worker_tags=None)
cluster.start_remote_worker(worker_tags=[_COLOCATED_WORKER_TAG])
expect_num_workers_to_read = num_local_workers + 2

# Wait for the new worker to register with the dispatcher.
while cluster._dispatcher._num_workers() < (num_local_workers +
                                            num_remote_workers + 4):
    time.sleep(10 / 1000)  # 10ms

results += self.getIteratorOutput(get_next)
self.assertCountEqual(
    results, expect_num_workers_to_read * list(range(num_elements)))
