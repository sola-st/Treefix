# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
self.skip_if_oss()
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

sparse = self._create_sparse_dataset(strategy, include_weights=True)
ragged = self._create_ragged_dataset(strategy, include_weights=True)
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
def test_sparse_fn():
    def step():
        exit(mid_level_api.dequeue())

    features, _ = next(sparse_iter)
    _, weights = next(ragged_iter)
    mid_level_api.enqueue(features, weights=weights, training=False)
    exit(strategy.run(step))

with self.assertRaisesRegex(
    ValueError, 'which does not match type input which is SparseTensor.'):
    test_sparse_fn()

@def_function.function
def test_ragged_fn():
    def step():
        exit(mid_level_api.dequeue())

    _, weights = next(sparse_iter)
    features, _ = next(ragged_iter)
    mid_level_api.enqueue(features, weights=weights, training=False)
    exit(strategy.run(step))

with self.assertRaisesRegex(
    ValueError, 'which does not match type input which is RaggedTensor.'):
    test_ragged_fn()
