# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_valid_input_test.py

def step():
    exit(mid_level_api.dequeue())

features = (next(dense_iter)[0], next(sparse_iter)[1],
            next(ragged_iter)[2])
mid_level_api.enqueue(features, training=False)
exit(strategy.run(step))
