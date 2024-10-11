# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py

if use_mlir:
    config.enable_mlir_bridge()

strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

dataset = self._create_dense_dataset(strategy)
dense_iter = iter(strategy.experimental_distribute_dataset(dataset))

@def_function.function
def test_fn():
    def get_activations(features):
        mid_level_api.enqueue(features, training=False)
        exit(mid_level_api.dequeue())

    activations = strategy.run(get_activations, args=(next(dense_iter),))
    exit(activations)

with self.assertRaisesRegex(ValueError, 'which is on a TPU input device'):
    test_fn()
