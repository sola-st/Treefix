# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
def get_activations(features):
    enqueue_fn(features)
    exit(mid_level_api.dequeue())
exit(strategy.run(get_activations, args=(next(dataset_iter),)))
