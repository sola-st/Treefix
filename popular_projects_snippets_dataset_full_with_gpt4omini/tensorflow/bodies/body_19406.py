# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
self.skip_if_oss()
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

sparse = self._create_sparse_dataset(strategy, include_weights=True)
sparse_iter = iter(
    strategy.experimental_distribute_dataset(
        sparse,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def test_features_fn():
    def step():
        exit(mid_level_api.dequeue())

    features = next(sparse_iter)
    features = (features[0],)
    mid_level_api.enqueue(features, training=False)
    exit(strategy.run(step))

# The error here is raised from nest.assert_same_structure
with self.assertRaises(ValueError):
    test_features_fn()

@def_function.function
def test_weights_fn():
    def step():
        exit(mid_level_api.dequeue())

    features, weights = next(sparse_iter)
    weights = (weights[0],)
    mid_level_api.enqueue(features, weights=weights, training=False)
    exit(strategy.run(step))

# The error here is raised from nest.assert_same_structure
with self.assertRaises(ValueError):
    test_weights_fn()
