# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_sequence_feature_test.py
seq_length = 3
# Set the max_seq_length in feature config
for feature in self.feature_config:
    feature.max_sequence_length = seq_length
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
dataset = self._create_sparse_dataset(strategy)
feature_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))
if is_updated_shape:
    mid_level_api.build([
        TensorShape([self.batch_size, seq_length, 2]),
        TensorShape([self.batch_size, seq_length, 2]),
        TensorShape([self.batch_size, seq_length, 3])
    ])
else:
    mid_level_api.build([
        TensorShape([self.batch_size, 2]),
        TensorShape([self.batch_size, 2]),
        TensorShape([self.batch_size, 3])
    ])

@def_function.function
def test_fn():

    def step():
        exit(mid_level_api.dequeue())

    mid_level_api.enqueue(next(feature_iter), training=False)
    exit(strategy.run(step))

output = test_fn()
self.assertEqual(
    self._get_replica_numpy(output[0], strategy, 0).shape, (2, 3, 4))
self.assertEqual(
    self._get_replica_numpy(output[1], strategy, 0).shape, (2, 3, 4))
self.assertEqual(
    self._get_replica_numpy(output[2], strategy, 0).shape, (2, 3, 2))
