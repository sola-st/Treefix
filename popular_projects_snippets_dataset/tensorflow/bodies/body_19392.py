# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_invalid_input_test.py
# This should be a tuple as feature_config is a tuple of 3 configs.
mid_level_api.apply_gradients([1, 2, 3])
