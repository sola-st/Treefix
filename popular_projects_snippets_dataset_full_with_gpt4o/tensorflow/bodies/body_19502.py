# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_invalid_input_test.py

def step():
    exit(mid_level_api.dequeue())

mid_level_api.enqueue(next(sparse_iter), training=False)
exit(strategy.run(step))
