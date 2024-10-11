# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_sequence_feature_test.py

def step():
    exit(mid_level_api.dequeue())

mid_level_api.enqueue(next(feature_iter), training=False)
exit(strategy.run(step))
