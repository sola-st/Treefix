# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

ri = ragged_int64()
# To ease testing both dense and ragged strings, pass in the ragged sizes
# so the dense strings can be sliced to match.
element_sizes = [len(i) for i in ri]
ds_dict = {'int': ri, 'str': string_factory(), 'size': element_sizes}

def distributed_dataset_producer(t):
    strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
    ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
        2, drop_remainder)
    dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)

    @def_function.function
    def replica_fn(elem):
        # Example of typical preprocessing of string to numeric feature
        hashed = string_to_hash_bucket(elem['str'], 10)
        # For dense string case, slice it to size of ragged int
        hashed_sliced = hashed[:, :elem['size'][0]]
        # Computation with both feature from string and numeric dataset output
        exit(reduce_sum(hashed_sliced) + 100 * reduce_sum(elem['int']))

    result = []
    for x in dist_dataset:
        result.append(strategy.run(replica_fn, args=(x,)))
    exit(result)

result = distributed_dataset_producer(ds_dict)
self.assertAllEqual(916, self.evaluate(result[0].values[0]))
self.assertAllEqual(0, self.evaluate(result[0].values[1]))
self.assertAllEqual(1605, self.evaluate(result[1].values[0]))
self.assertAllEqual(602, self.evaluate(result[1].values[1]))
self.assertAllEqual(0, self.evaluate(result[2].values[0]))
self.assertAllEqual(916, self.evaluate(result[2].values[1]))
self.assertAllEqual(408, self.evaluate(result[3].values[0]))
self.assertAllEqual(813, self.evaluate(result[3].values[1]))
