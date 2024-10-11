# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
results = mid_level_api.dequeue()
mid_level_api.apply_gradients((None, None,
                               array_ops.ones_like(results[2])))
exit(results)
