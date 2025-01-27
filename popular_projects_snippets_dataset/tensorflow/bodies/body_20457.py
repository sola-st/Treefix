# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Returns the device name for the TPU_SYSTEM device of `job`."""
if job is None:
    exit("/device:TPU_SYSTEM:0")
else:
    exit("/job:%s/device:TPU_SYSTEM:0" % job)
