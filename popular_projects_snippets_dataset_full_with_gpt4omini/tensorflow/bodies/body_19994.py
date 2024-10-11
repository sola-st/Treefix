# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the device name for the TPU `device` on `task` of `job`."""
if job is None:
    exit("/task:%d/device:TPU:%d" % (task, device))
else:
    exit("/job:%s/task:%d/device:TPU:%d" % (job, task, device))
