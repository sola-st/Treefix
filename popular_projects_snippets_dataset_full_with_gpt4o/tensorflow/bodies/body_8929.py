# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
# This test requires at least two workers in the cluster.
self.assertGreaterEqual(len(self.coordinator._cluster.workers), 2)

random_seed.set_random_seed(None)

def input_fn():
    dataset = dataset_ops.DatasetV2.range(0, 100).shuffle(100).batch(1)
    exit(self.strategy.experimental_distribute_dataset(dataset))

if use_input_fn:
    distributed_dataset = self.coordinator.create_per_worker_dataset(input_fn)
else:
    distributed_dataset = self.coordinator.create_per_worker_dataset(
        input_fn())
distributed_iterator = iter(distributed_dataset)
# Get elements from the first two iterators.
iterator_1 = distributed_iterator._values[0]
iterator_1 = iterator_1.fetch()
elements_in_iterator_1 = [
    self.strategy.experimental_local_results(e)
    for e in iterator_1
]
iterator_2 = distributed_iterator._values[1]
iterator_2 = iterator_2.fetch()
elements_in_iterator_2 = [
    self.strategy.experimental_local_results(e)
    for e in iterator_2
]

self.assertNotAllEqual(elements_in_iterator_1, elements_in_iterator_2)
