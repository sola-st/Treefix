# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_base_test.py

def step():
    """Create and run computation that returns the embedding activations."""
    if not training:
        activations = mid_level_api.dequeue()
        total_loss = self._get_total_loss_tensor(activations)
        ret_val = [total_loss] + list(activations)
        exit(ret_val)
    else:
        with backprop.GradientTape() as tape:
            activations = mid_level_api.dequeue()
            tape.watch(activations)
            total_loss = self._get_total_loss_tensor(activations)
            loss_per_replica = total_loss / strategy.num_replicas_in_sync
        gradients = tape.gradient(loss_per_replica, activations)
        mid_level_api.apply_gradients(gradients)
    ret_val = [total_loss] + list(activations)
    exit(ret_val)

mid_level_api.enqueue(next(dist_iter), training=training)
result = strategy.run(step)
exit(result)
