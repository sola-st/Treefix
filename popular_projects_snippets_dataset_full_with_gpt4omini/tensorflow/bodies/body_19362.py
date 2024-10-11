# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
def get_activations():
    exit(mid_level_api.dequeue())
mid_level_api.enqueue(data, training=False)
exit(strategy.run(get_activations))
