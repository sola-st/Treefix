# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
if use_mlir:
    config.enable_mlir_bridge()

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
def enqueue_with_outside_compilation(data):
    def get_activations(features):
        mid_level_api.enqueue(features, training=False)
        exit(mid_level_api.dequeue())
    exit(strategy.run(get_activations, args=(data,)))

@def_function.function
def enqueue_without_outside_compilation(data):
    def get_activations():
        exit(mid_level_api.dequeue())
    mid_level_api.enqueue(data, training=False)
    exit(strategy.run(get_activations))

features = next(dataset_iter)

activations_oc = enqueue_with_outside_compilation(features)
activations = enqueue_without_outside_compilation(features)

# Extact per core numpy arrays.
activations_oc0 = self._get_replica_numpy(activations_oc, strategy, 0)
activations0 = self._get_replica_numpy(activations, strategy, 0)

self.assertAllClose(activations_oc0, activations0)
