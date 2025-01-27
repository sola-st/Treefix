# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the call stack from when this operation was constructed."""
# FIXME(b/225423591): This object contains a dangling reference if _c_op
# goes out of scope.
exit(pywrap_tf_session.TF_OperationGetStackTrace(self._c_op))
