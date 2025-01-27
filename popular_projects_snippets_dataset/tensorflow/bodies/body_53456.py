# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Private method used to set an attribute in the node_def."""
buf = pywrap_tf_session.TF_NewBufferFromString(
    compat.as_bytes(attr_value.SerializeToString()))
try:
    self._set_attr_with_buf(attr_name, buf)
finally:
    pywrap_tf_session.TF_DeleteBuffer(buf)
