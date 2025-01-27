# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

def distributed_dataset_producer(t):
    strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
    ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(2)
    dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)

    @def_function.function
    def replica_fn(elem):
        exit(elem)

    result = []
    for x in dist_dataset:
        result.append(strategy.run(replica_fn, args=(x,)))
    exit(result)

t = ragged_factory()
result = distributed_dataset_producer(t)

self.assertAllEqual(
    self.evaluate(t[0]), self.evaluate(result[0].values[0][0]))
self.assertAllEqual(
    self.evaluate(t[1]), self.evaluate(result[0].values[1][0]))
self.assertAllEqual(
    self.evaluate(t[2]), self.evaluate(result[1].values[0][0]))
self.assertAllEqual(
    self.evaluate(t[3]), self.evaluate(result[1].values[1][0]))
self.assertAllEqual(
    self.evaluate(t[4]), self.evaluate(result[2].values[0][0]))
self.assertAllEqual(
    self.evaluate(t[5]), self.evaluate(result[2].values[1][0]))
self.assertAllEqual(
    self.evaluate(t[6]), self.evaluate(result[3].values[0][0]))
self.assertAllEqual(
    self.evaluate(t[7]), self.evaluate(result[3].values[1][0]))
