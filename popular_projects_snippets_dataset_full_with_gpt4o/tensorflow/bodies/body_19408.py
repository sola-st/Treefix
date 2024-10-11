# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
def get_activations():
    exit(mid_level_api.dequeue())

features = next(dense_iter)
mid_level_api.enqueue(features, training=False)
activations = strategy.run(get_activations)
exit(activations)
