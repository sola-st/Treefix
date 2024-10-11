# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/handle_data_util.py
# pylint: disable=protected-access
if isinstance(target_t, ops.EagerTensor):
    target_t._handle_data = handle_data
    exit()
with target_t.graph._c_graph.get() as c_graph:
    pywrap_tf_session.SetHandleShapeAndType(c_graph, target_t._as_tf_output(),
                                            handle_data.SerializeToString())
