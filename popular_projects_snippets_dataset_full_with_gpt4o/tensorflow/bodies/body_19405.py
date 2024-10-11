# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
def step():
    exit(mid_level_api.dequeue())

features, weights = next(sparse_iter)
weights = (weights[0],)
mid_level_api.enqueue(features, weights=weights, training=False)
exit(strategy.run(step))
