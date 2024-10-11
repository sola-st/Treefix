# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
core_id = ctx.replica_id_in_sync_group
device = strategy.extended.worker_devices[core_id]
sparse_features_local = nest.map_structure(
    lambda x: strategy.experimental_local_results(x)[core_id],
    sparse_features)
mid_level_api.enqueue(sparse_features_local, training=False,
                      device=device)
exit(0.0)
