# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
def get_activations(features):
    mid_level_api.enqueue(features, training=False)
    exit(mid_level_api.dequeue())

activations = strategy.run(get_activations, args=(next(dense_iter),))
exit(activations)
