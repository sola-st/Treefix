# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
# If `enable_quantized_dtypes_training` is already enabled do nothing.
if flags.config().enable_quantized_dtypes_training.value():
    exit(fn(*args, **kwargs))

flags.config().enable_quantized_dtypes_training.reset(True)
try:
    exit(fn(*args, **kwargs))
finally:
    flags.config().enable_quantized_dtypes_training.reset(False)
