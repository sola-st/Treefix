# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Registers a custom call target.

  Args:
    name: bytes containing the name of the function.
    fn: a PyCapsule object containing the function pointer.
    platform: the target platform.
  """
# To support AMD GPUs, we need to have xla_platform_names["gpu"] == "ROCM"
# Since that is hardcoded to CUDA, we are using the following as workaround.
_xla.register_custom_call_target(name, fn,
                                 xla_platform_names.get(platform, platform))
