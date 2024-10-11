# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
weight = 0.5
if ragged:
    dataset = self._create_ragged_dataset(strategy, include_weights=True,
                                          weight=weight)
else:
    dataset = self._create_sparse_dataset(strategy, include_weights=True,
                                          weight=weight)
    mid_level_api.build([
        TensorShape((self.batch_size, 2)),
        TensorShape((self.batch_size, 2)),
        TensorShape((self.batch_size, 3))
    ])

dataset_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def enqueue_and_get(features, weights):
    def get_activations():
        exit(mid_level_api.dequeue())
    mid_level_api.enqueue(features, weights=weights, training=False)
    exit(strategy.run(get_activations))

features, weights = next(dataset_iter)
# Replace the weight for the second feature by None to test.
weights = (weights[0], None, weights[2])

no_weights_activations = enqueue_and_get(features, weights=None)
weights_activations = enqueue_and_get(features, weights=weights)

# Extact per core numpy arrays.
no_weights0 = self._get_replica_numpy(no_weights_activations, strategy, 0)
weights0 = self._get_replica_numpy(weights_activations, strategy, 0)
# videos table has sum combiner and users table has mean combiner.
# i.e. users table lookups isn't affected by the weights as all the weights
# are the same.
# Tuple entry 0 and 1 are the watched and favorited features from the videos
# table and entry 2 is the friends feature from the users table.
# Note that None was passed as a weight for entry 1 so weight should have no
# effect.
weight = (0.5, 1.0, 1.0)
golden = tuple([no_weight * w for no_weight, w in zip(no_weights0, weight)])

self.assertAllClose(golden, weights0)
