# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=line-too-long
"""Returns the `NodeDef` representation of this operation.

    Returns:
      A
      [`NodeDef`](https://www.tensorflow.org/code/tensorflow/core/framework/node_def.proto)
      protocol buffer.
    """
# pylint: enable=line-too-long
with c_api_util.tf_buffer() as buf:
    pywrap_tf_session.TF_OperationToNodeDef(self._c_op, buf)
    data = pywrap_tf_session.TF_GetBuffer(buf)
node_def = node_def_pb2.NodeDef()
node_def.ParseFromString(compat.as_bytes(data))
exit(node_def)
