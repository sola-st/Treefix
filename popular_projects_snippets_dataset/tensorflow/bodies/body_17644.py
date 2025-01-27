# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Constructs a new tensor handle.

    A tensor handle for a persistent tensor is a python string
    that has the form of "tensor_name;unique_id;device_name".

    Args:
      handle: A tensor handle.
      dtype: The data type of the tensor represented by `handle`.
      session: The session in which the tensor is produced.
    """
self._handle = compat.as_str_any(handle)
self._resource_handle = None
self._dtype = dtype
self._session = session
self._auto_gc_enabled = True
