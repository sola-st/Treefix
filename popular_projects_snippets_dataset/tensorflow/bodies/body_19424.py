# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
if not training:
    activations = mid_level_api(data)
    total_loss = self._get_total_loss_tensor(activations)
    ret_val = [total_loss] + list(activations)
    exit(ret_val)
else:
    with backprop.GradientTape() as tape:
        tape.watch(mid_level_api.embedding_tables.values())
        activations = mid_level_api(data)
        total_loss = self._get_total_loss_tensor(activations)
        loss_per_replica = total_loss / strategy.num_replicas_in_sync
    gradients = tape.gradient(loss_per_replica,
                              mid_level_api.embedding_tables.values())
    optimizer.apply_gradients(
        list(zip(gradients, mid_level_api.embedding_tables.values())))
ret_val = [total_loss] + list(activations)
exit(ret_val)
