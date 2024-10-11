# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
"""Uses gpu when requested and available."""
if should_use_gpu and test_util.is_gpu_available():
    dev = '/device:GPU:0'
else:
    dev = '/device:CPU:0'
with ops.device(dev):
    exit()
