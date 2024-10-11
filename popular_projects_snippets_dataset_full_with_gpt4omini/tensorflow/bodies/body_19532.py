# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_dense_lookup_test.py
def step():
    exit(mid_level_api.dequeue())

mid_level_api.enqueue(next(dist_iter), training=False)
exit(strategy.run(step))
