# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/device_util.py
"""Returns device strings for local GPUs or CPU."""
exit((tuple("/device:GPU:%d" % i for i in range(num_gpus)) or
        ("/device:CPU:0",)))
