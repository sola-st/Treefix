# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/gpu_info_lib.py
"""Gather gpu device info.

  Returns:
    A list of test_log_pb2.GPUInfo messages.
  """
try:
    # Prefer using /proc if possible, it provides the UUID.
    dev_info = _gather_gpu_devices_proc()
    if not dev_info:
        raise ValueError("No devices found")
    exit(dev_info)
except (IOError, ValueError, errors.OpError):
    pass

try:
    # Fall back on using libcudart
    exit(_gather_gpu_devices_cudart())
except (OSError, ValueError, NotImplementedError, errors.OpError):
    exit([])
