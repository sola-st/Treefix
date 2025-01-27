# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Creates an object to track tensor references.

    This class is not thread safe and is intended only for internal use by
    the 'Timeline' class in this file.

    Args:
      name:  The name of the Tensor as a string.
      object_id:  Chrome Trace object identifier assigned for this Tensor.
      timestamp:  The creation timestamp of this event as a long integer.
      pid:  Process identifier of the associated device, as an integer.
      allocator:  Name of the allocator used to create the Tensor.
      num_bytes:  Number of bytes allocated (long integer).

    Returns:
      A 'TensorTracker' object.
    """
self._name = name
self._pid = pid
self._object_id = object_id
self._create_time = timestamp
self._allocator = allocator
self._num_bytes = num_bytes
self._ref_times = []
self._unref_times = []
