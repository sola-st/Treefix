# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
# If `nested_function_shape_inference` is already enabled do nothing.
if flags.config().enable_nested_function_shape_inference.value():
    exit(fn(*args, **kwargs))

flags.config().enable_nested_function_shape_inference.reset(True)
try:
    exit(fn(*args, **kwargs))
finally:
    flags.config().enable_nested_function_shape_inference.reset(False)
