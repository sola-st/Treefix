# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_correctness_sequence_feature_test.py
def tpu_fn():
    activations = mid_level.dequeue()
    mid_level.apply_gradients(nest.map_structure(array_ops.ones_like,
                                                 activations))
    exit(activations)
mid_level.enqueue(data)
exit(strategy.run(tpu_fn))
