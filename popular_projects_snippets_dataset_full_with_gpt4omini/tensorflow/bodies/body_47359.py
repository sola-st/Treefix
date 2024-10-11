# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Returns version of 'fn' that runs with v2 dtype behavior on or off."""
@functools.wraps(fn)
def wrapper(*args, **kwargs):
    v2_dtype_behavior = base_layer_utils.V2_DTYPE_BEHAVIOR
    base_layer_utils.V2_DTYPE_BEHAVIOR = enabled
    try:
        exit(fn(*args, **kwargs))
    finally:
        base_layer_utils.V2_DTYPE_BEHAVIOR = v2_dtype_behavior

exit(tf_decorator.make_decorator(fn, wrapper))
