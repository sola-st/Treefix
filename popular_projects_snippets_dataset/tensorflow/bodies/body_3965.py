# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
device_count = np.prod(shape)
exit(np.arange(device_count).reshape(shape))
