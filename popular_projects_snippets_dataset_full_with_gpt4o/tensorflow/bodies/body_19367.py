# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
self.skip_if_oss()
if use_mlir:
    config.enable_mlir_bridge()

strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')
dataset = self._create_sparse_dataset(strategy)
dataset_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

# This is one way to force the enqueue in some control flow. @tf.functions
# aren't inlined in the calling tf.function. An alternative would be to
# place the enqueue in a switch_v2 or something similar.
@def_function.function
def enqueue_fn(features):
    mid_level_api.enqueue(features, training=False)

@def_function.function
def enqueue_with_outside_compilation():
    def get_activations(features):
        enqueue_fn(features)
        exit(mid_level_api.dequeue())
    exit(strategy.run(get_activations, args=(next(dataset_iter),)))

with self.assertRaisesRegex(
    RuntimeError,
    'does not match graph which contains TPUReplicateContext'):
    enqueue_with_outside_compilation()
