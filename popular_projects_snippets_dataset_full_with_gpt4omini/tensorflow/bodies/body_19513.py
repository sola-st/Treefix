# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
self.skip_if_oss()
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

sparse = self._create_sparse_dataset(strategy)
ragged = self._create_ragged_dataset(strategy)
sparse_iter = iter(
    strategy.experimental_distribute_dataset(
        sparse,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))
ragged_iter = iter(
    strategy.experimental_distribute_dataset(
        ragged,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def test_fn():
    def step():
        exit(mid_level_api.dequeue())

    sparse_features = next(sparse_iter)
    ragged_features = next(ragged_iter)
    features = (sparse_features[0], ragged_features[1], sparse_features[2])
    mid_level_api.enqueue(features, training=False)
    exit(strategy.run(step))

test_fn()
