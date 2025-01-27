# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Constructor.

    Args:
      tensor_proto: the `TensorProto` object that cannot be represented as a
        `np.ndarray` object.
      initialized: (`bool`) whether the Tensor is initialized.
    """
self._tensor_proto = tensor_proto
self._initialized = initialized
