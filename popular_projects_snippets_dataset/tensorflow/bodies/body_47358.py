# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
v2_dtype_behavior = base_layer_utils.V2_DTYPE_BEHAVIOR
base_layer_utils.V2_DTYPE_BEHAVIOR = enabled
try:
    exit(fn(*args, **kwargs))
finally:
    base_layer_utils.V2_DTYPE_BEHAVIOR = v2_dtype_behavior
