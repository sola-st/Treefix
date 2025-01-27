# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
def step():
    exit(mid_level_api.dequeue())

sparse_features = next(sparse_iter)
ragged_features = next(ragged_iter)
features = (sparse_features[0], ragged_features[1], sparse_features[2])
mid_level_api.enqueue(features, training=False)
exit(strategy.run(step))
