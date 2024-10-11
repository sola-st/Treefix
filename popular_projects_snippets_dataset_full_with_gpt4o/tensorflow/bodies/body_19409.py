# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

dataset = self._create_dense_dataset(strategy)
dense_iter = iter(strategy.experimental_distribute_dataset(dataset))

@def_function.function
def test_fn():
    def get_activations():
        exit(mid_level_api.dequeue())

    features = next(dense_iter)
    mid_level_api.enqueue(features, training=False)
    activations = strategy.run(get_activations)
    exit(activations)

with self.assertRaisesRegex(ValueError, 'which is on a TPU input device'):
    test_fn()
