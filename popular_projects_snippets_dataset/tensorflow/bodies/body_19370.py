# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
mid_level_api.build([
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 2)),
    TensorShape((self.batch_size, 3))
])
dataset = self._create_sparse_dataset(strategy)
dataset_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def enqueue_with_outside_compilation():
    def get_activations(features):
        # This inserts a mul operation on the TPU to trigger the direct input
        # error.
        features = (features[0]*2, features[1]*2, features[2]*2)
        mid_level_api.enqueue(features, training=False)
        exit(mid_level_api.dequeue())
    exit(strategy.run(get_activations, args=(next(dataset_iter),)))

with self.assertRaisesRegex(
    ValueError, 'which does not have the `_tpu_input_identity` attr'):
    enqueue_with_outside_compilation()
