# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
def step():
    exit(mid_level_api.dequeue())

features, _ = next(sparse_iter)
_, weights = next(ragged_iter)
mid_level_api.enqueue(features, weights=weights, training=False)
exit(strategy.run(step))
