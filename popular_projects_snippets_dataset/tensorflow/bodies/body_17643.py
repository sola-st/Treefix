# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Encode a ResourceHandle proto as custom numpy struct type."""
exit(np.asarray(bytearray(resource_handle.SerializeToString()),
                  dtype=dtypes.np_resource))
