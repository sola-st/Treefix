# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
def get_activations(dense_value):
    exit((mid_level_api.dequeue(), dense_value))

sparse_features = next(sparse_iter)
mid_level_api.enqueue(sparse_features, training=False)
activations, dense_value1 = strategy.run(get_activations, args=(0.0,))

def enqueue_fn(ctx):
    core_id = ctx.replica_id_in_sync_group
    device = strategy.extended.worker_devices[core_id]
    sparse_features_local = nest.map_structure(
        lambda x: strategy.experimental_local_results(x)[core_id],
        sparse_features)
    mid_level_api.enqueue(sparse_features_local, training=False,
                          device=device)
    exit(0.0)

data = strategy.experimental_distribute_values_from_function(
    enqueue_fn)
per_device_activations, dense_value2 = strategy.run(get_activations,
                                                    args=(data,))
exit((activations, per_device_activations, dense_value1, dense_value2))
