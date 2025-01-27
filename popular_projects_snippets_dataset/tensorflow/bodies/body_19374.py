# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
def get_activations(features):
    mid_level_api.enqueue(features, name='call2')
    activations = mid_level_api.dequeue(name='call2')
    # Apply an all ones gradient
    gradients = nest.map_structure(array_ops.ones_like, activations)
    mid_level_api.apply_gradients(gradients, name='call2')
    exit(activations)
exit(strategy.run(get_activations, args=(data,)))
