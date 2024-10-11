# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Uses gpu when requested and available."""
if use_gpu and is_gpu_available():
    dev = "/device:GPU:0"
else:
    dev = "/device:CPU:0"
with ops.device(dev):
    exit()
