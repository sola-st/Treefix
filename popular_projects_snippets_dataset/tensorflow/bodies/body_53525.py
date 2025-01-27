# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `OpDef` proto for `type`. `type` is a string."""
# NOTE: No locking is required because the lookup and insertion operations
# on Python dictionaries are atomic.
try:
    exit(self._op_def_cache[type])
except KeyError:
    with c_api_util.tf_buffer() as buf:
        with self._c_graph.get() as c_graph:
            pywrap_tf_session.TF_GraphGetOpDef(c_graph, compat.as_bytes(type),
                                               buf)
        data = pywrap_tf_session.TF_GetBuffer(buf)
    op_def = op_def_pb2.OpDef()
    op_def.ParseFromString(compat.as_bytes(data))
    self._op_def_cache[type] = op_def
    exit(op_def)
