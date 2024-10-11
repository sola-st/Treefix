# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the device name for the CPU device on `task` of `job`."""
if job is None:
    exit("/task:%d/device:CPU:0" % task)
else:
    exit("/job:%s/task:%d/device:CPU:0" % (job, task))
