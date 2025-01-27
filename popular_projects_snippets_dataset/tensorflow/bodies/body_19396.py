# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

dataset = self._create_dense_dataset(strategy, include_weights=True)
dense_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def test_fn():
    def step():
        exit(mid_level_api.dequeue())

    features, weights = next(dense_iter)
    mid_level_api.enqueue(features, weights=weights, training=False)
    exit(strategy.run(step))

with self.assertRaisesRegex(ValueError, 'Weight specified for dense input'):
    test_fn()
