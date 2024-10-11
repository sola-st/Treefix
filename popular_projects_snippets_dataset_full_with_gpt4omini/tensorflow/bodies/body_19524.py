# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py

def get_activations():
    exit(mid_level_api.dequeue())

mid_level_api.enqueue(next(dataset_iter), training=False)
exit(strategy.run(get_activations))
