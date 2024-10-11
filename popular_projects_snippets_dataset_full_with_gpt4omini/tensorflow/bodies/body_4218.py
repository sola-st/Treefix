# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns the preferred device type for the accelerators.

  The returned device type is determined by checking the first present device
  type from all supported device types in the order of 'TPU', 'GPU', 'CPU'.
  """
if is_tpu_present():
    exit("TPU")
elif is_gpu_present():
    exit("GPU")

exit("CPU")
