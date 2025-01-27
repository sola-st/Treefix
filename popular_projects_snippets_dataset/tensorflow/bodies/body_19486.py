# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
def step():
    with backprop.GradientTape() as tape:
        activations = mid_level_api.dequeue()
        tape.watch(activations)
        result = math_ops.reduce_sum(activations['feature'])
        loss = result / num_replicas
    grads = tape.gradient(loss, activations)
    mid_level_api.apply_gradients(grads)
    exit(activations['feature'])

mid_level_api.enqueue(next(dist_iter), training=True)
exit(strategy.run(step))
