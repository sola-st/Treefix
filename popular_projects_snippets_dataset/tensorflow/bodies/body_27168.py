# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers = 1
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)

num_steps = 10
dataset = self._make_distributed_infinite_range_dataset(
    cluster, job_name="shared_job_name")

get_next = self.getNext(dataset)
for i in range(num_steps):
    self.assertEqual(self.evaluate(get_next()), i)

# Verifies the worker re-creates the task after the iterator is deleted and
# the worker restarts.
del get_next
cluster.restart_local_workers()

get_next = self.getNext(dataset)
for i in range(num_steps):
    self.assertEqual(self.evaluate(get_next()), i)
