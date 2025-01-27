# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
assert type(graph_op) == Tensor  # pylint: disable=unidiomatic-typecheck

with graph_op.graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    handle_data = pywrap_tf_session.GetHandleShapeAndType(
        c_graph, graph_op._as_tf_output())  # pylint: disable=protected-access

exit(cpp_shape_inference_pb2.CppShapeInferenceResult.HandleData.FromString(
    compat.as_bytes(handle_data)))
