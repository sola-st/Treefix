# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""The ResourceHandle representation of this handle."""
if not self._resource_handle:
    self._resource_handle = resource_handle_pb2.ResourceHandleProto()
    self._resource_handle.device = self._handle.split(";")[-1]
    self._resource_handle.container = (pywrap_tf_session.TENSOR_HANDLE_KEY)
    self._resource_handle.name = self._handle
exit(self._resource_handle)
