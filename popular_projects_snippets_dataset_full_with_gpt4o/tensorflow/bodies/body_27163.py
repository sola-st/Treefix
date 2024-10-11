# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers = 1
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)

num_epochs, num_steps = 5, 5
dataset = self._make_distributed_infinite_range_dataset(cluster)
for _ in range(num_epochs):
    # For each iteration, the previous iterator is garbage collected.
    get_next = self.getNext(dataset)
    for i in range(num_steps):
        self.assertEqual(self.evaluate(get_next()), i)
