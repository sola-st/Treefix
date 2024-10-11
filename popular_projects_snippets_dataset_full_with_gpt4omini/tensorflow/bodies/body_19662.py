# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_name_util.py
"""Returns the device name for a core in a replicated TPU computation.

  Args:
    num: the virtual core number within each replica to which operators should
    be assigned.
  Returns:
    A device name, suitable for passing to `tf.device()`.
  """
exit("device:TPU_REPLICATED_CORE:{}".format(num))
