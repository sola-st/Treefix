# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/errors_impl.py
"""Creates a new `OpError` indicating that a particular op failed.

    Args:
      node_def: The `node_def_pb2.NodeDef` proto representing the op that
        failed, if known; otherwise None.
      op: The `ops.Operation` that failed, if known; otherwise None. During
        eager execution, this field is always `None`.
      message: The message string describing the failure.
      error_code: The `error_codes_pb2.Code` describing the error.
      *args: If not empty, it should contain a dictionary describing details
        about the error. This argument is inspired by Abseil payloads:
        https://github.com/abseil/abseil-cpp/blob/master/absl/status/status.h
    """
super(OpError, self).__init__()
self._node_def = node_def
self._op = op
self._message = message
self._error_code = error_code
if args:
    self._experimental_payloads = args[0]
else:
    self._experimental_payloads = {}
