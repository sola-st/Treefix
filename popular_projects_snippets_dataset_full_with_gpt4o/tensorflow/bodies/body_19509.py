# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
mid_level_api.enqueue(data, training=False)
def tpu_fn():
    exit(mid_level_api.dequeue())
exit(strategy.run(tpu_fn))
