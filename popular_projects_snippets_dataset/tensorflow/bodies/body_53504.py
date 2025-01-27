# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# pylint: disable=line-too-long
"""Returns a serialized `GraphDef` representation of this graph.

    The serialized `GraphDef` can be imported into another `Graph`
    (using `tf.import_graph_def`) or used with the
    [C++ Session API](https://chromium.googlesource.com/external/github.com/tensorflow/tensorflow/+/r0.10/tensorflow/g3doc/api_docs/cc/index.md).

    This method is thread-safe.

    Args:
      from_version: Optional.  If this is set, returns a `GraphDef` containing
        only the nodes that were added to this graph since its `version`
        property had the given value.
      add_shapes: If true, adds an "_output_shapes" list attr to each node with
        the inferred shapes of each of its outputs.

    Returns:
      A tuple containing a
      [`GraphDef`](https://www.tensorflow.org/code/tensorflow/core/framework/graph.proto)
      protocol buffer, and the version of the graph to which that
      `GraphDef` corresponds.

    Raises:
      ValueError: If the `graph_def` would be too large.

    """
# pylint: enable=line-too-long
with self._lock:
    with c_api_util.tf_buffer() as buf:
        with self._c_graph.get() as c_graph:
            pywrap_tf_session.TF_GraphToGraphDef(c_graph, buf)
            data = pywrap_tf_session.TF_GetBuffer(buf)
    graph = graph_pb2.GraphDef()
    graph.ParseFromString(compat.as_bytes(data))
    # Strip the experimental library field iff it's empty.
    if not graph.library.function:
        graph.ClearField("library")

    if add_shapes:
        for node in graph.node:
            op = self._nodes_by_name[node.name]
            if op.outputs:
                node.attr["_output_shapes"].list.shape.extend(
                    [output.get_shape().as_proto() for output in op.outputs])
        for function_def in graph.library.function:
            defined_function = self._functions[function_def.signature.name]
            try:
                func_graph = defined_function.graph
            except AttributeError:
                # _DefinedFunction doesn't have a graph, _EagerDefinedFunction
                # does. Both rely on ops.py, so we can't really isinstance check
                # them.
                continue
            input_shapes = function_def.attr["_input_shapes"]
            try:
                func_graph_inputs = func_graph.inputs
            except AttributeError:
                continue
            # TODO(b/141471245): Fix the inconsistency when inputs of func graph
            # are appended during gradient computation of while/cond.
            assert len(input_shapes.list.shape) in [0, len(func_graph_inputs)]
            # If the function_def has inputs already filled out, skip this step.
            if not input_shapes.list.shape:
                for input_tensor, arg_def in zip(func_graph_inputs,
                                                 function_def.signature.input_arg):
                    input_shapes.list.shape.add().CopyFrom(
                        input_tensor.get_shape().as_proto())
                    if input_tensor.dtype == dtypes.resource:
                        _copy_handle_data_to_arg_def(input_tensor, arg_def)

            for output_tensor, arg_def in zip(func_graph.outputs,
                                              function_def.signature.output_arg):
                if output_tensor.dtype == dtypes.resource:
                    _copy_handle_data_to_arg_def(output_tensor, arg_def)

            for node in function_def.node_def:
                try:
                    op = func_graph.get_operation_by_name(node.name)
                except KeyError:
                    continue
                outputs = op.outputs

                if op.type == "StatefulPartitionedCall":
                    # Filter out any extra outputs (possibly added by function
                    # backpropagation rewriting).
                    num_outputs = len(node.attr["Tout"].list.type)
                    outputs = outputs[:num_outputs]

                node.attr["_output_shapes"].list.shape.extend(
                    [output.get_shape().as_proto() for output in outputs])

exit((graph, self._version))
