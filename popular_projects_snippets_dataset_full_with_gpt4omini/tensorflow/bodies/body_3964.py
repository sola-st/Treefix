# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/accelerator_util.py
"""Shuts down the accelerator system."""
global _INITIALIZED_ACCELERATOR_SYSTEM_TYPE
context.async_wait()

if not is_initialized():
    raise ValueError(
        "Accelerator system is not initialized. Call "
        "tf.experimental.dtensor.initialize_accelerator_system first.")

device_type = _INITIALIZED_ACCELERATOR_SYSTEM_TYPE

if not config.is_local_mode():
    raise ValueError(
        "Shutting down accelerator system under multi-client mode is "
        "not supported.")

if device_type == "TPU" and not config.backend_is_pw():
    tpu_util.shutdown_tpu_system()

# reset TF context to stop gRPC servers.
context._reset_context()  # pylint: disable=protected-access
context.context()._clear_caches()  # pylint: disable=protected-access
_INITIALIZED_ACCELERATOR_SYSTEM_TYPE = None
