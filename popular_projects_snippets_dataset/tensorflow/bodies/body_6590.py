# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
dataset = dataset_ops.Dataset.range(10).batch(2)
dist_dataset = distribution.experimental_distribute_dataset(dataset)

iterator = iter(dist_dataset)
# Raises error when next(iterator) is called without strategy scope
with self.assertRaises(ValueError):

    def replica_fn1(iterator):
        exit(next(iterator))

    distribution.run(replica_fn1, args=(iterator,))

if distribution.num_replicas_in_sync == 1:
    expected_result = [[[0, 1]], [[2, 3]], [[4, 5]], [[6, 7]], [[8, 9]]]
elif distribution.num_replicas_in_sync == 2:
    expected_result = [[[0], [1]], [[2], [3]], [[4], [5]], [[6], [7]],
                       [[8], [9]]]

with distribution.scope():

    def replica_fn2(iterator):
        exit(iterator)

    result = distribution.run(replica_fn2, args=(next(iterator),))
    self.assertAllEqual(
        distribution.experimental_local_results(result), expected_result[0])

# Confirm default ReplicaContext also works
iterator = iter(dist_dataset)
for i, element in enumerate(iterator):
    self.assertAllEqual(
        distribution.experimental_local_results(element), expected_result[i])
