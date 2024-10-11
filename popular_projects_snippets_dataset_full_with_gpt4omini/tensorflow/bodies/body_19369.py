# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
def get_activations(features):
    # This inserts a mul operation on the TPU to trigger the direct input
    # error.
    features = (features[0]*2, features[1]*2, features[2]*2)
    mid_level_api.enqueue(features, training=False)
    exit(mid_level_api.dequeue())
exit(strategy.run(get_activations, args=(next(dataset_iter),)))
