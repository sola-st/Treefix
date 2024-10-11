# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

def distributed_dataset_producer(t):
    strategy = mirrored_strategy.MirroredStrategy(['GPU:0', 'GPU:1'])
    ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
        2, drop_remainder)
    dist_dataset = strategy.experimental_distribute_dataset(ragged_ds)

    @def_function.function
    def replica_fn(elem):
        # Example of typical preprocessing of string to numeric feature
        hashed = string_to_hash_bucket(elem['str'], 10)
        exit(1000 * hashed)

    result = []
    for x in dist_dataset:
        result.append(strategy.run(replica_fn, args=(x,)))
    exit(result)

ds_dict = {'str': string_factory()}
result = distributed_dataset_producer(ds_dict)
expect_length = [len(i) for i in ds_dict['str']]
self.assertAllEqual([[5000, 3000, 5000, 3000][:expect_length[0]]],
                    self.evaluate(result[0].values[0]))
self.assertAllEqual([[9000, 9000, 9000, 9000][:expect_length[1]]],
                    self.evaluate(result[0].values[1]))
self.assertAllEqual([[0, 3000, 2000, 9000][:expect_length[2]]],
                    self.evaluate(result[1].values[0]))
self.assertAllEqual([[2000, 9000, 9000, 9000][:expect_length[3]]],
                    self.evaluate(result[1].values[1]))
self.assertAllEqual([[9000, 9000, 9000, 9000][:expect_length[4]]],
                    self.evaluate(result[2].values[0]))
self.assertAllEqual([[5000, 3000, 5000, 3000][:expect_length[5]]],
                    self.evaluate(result[2].values[1]))
self.assertAllEqual([[5000, 3000, 9000, 9000][:expect_length[6]]],
                    self.evaluate(result[3].values[0]))
self.assertAllEqual([[2000, 3000, 5000, 3000][:expect_length[7]]],
                    self.evaluate(result[3].values[1]))
