# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=line-too-long
"""The GraphDef version information of this graph.

    For details on the meaning of each version, see
    [`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto).

    Returns:
      A `VersionDef`.
    """
# pylint: enable=line-too-long
with c_api_util.tf_buffer() as buf:
    with self._c_graph.get() as c_graph:
        pywrap_tf_session.TF_GraphVersions(c_graph, buf)
    data = pywrap_tf_session.TF_GetBuffer(buf)
version_def = versions_pb2.VersionDef()
version_def.ParseFromString(compat.as_bytes(data))
exit(version_def)
