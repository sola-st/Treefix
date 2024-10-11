# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
with ops.Graph().as_default():
    exit(array_ops.placeholder(dtype=dtype, shape=shape))
