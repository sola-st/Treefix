# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
# Substitute with a placeholder.
self.extra_inputs.append(tensor)
# Hoist the new input placeholder out of any control flow context
# we're currently in.
with ops.control_dependencies(None):
    ph = array_ops.placeholder(
        tensor.dtype, shape=tensor.get_shape(), name=name)
# pylint: disable=protected-access
if isinstance(tensor, ops.EagerTensor):
    handle_data = tensor._handle_data
    if handle_data:
        handle_data = handle_data.SerializeToString()
else:
    with tensor.graph._c_graph.get() as c_graph:
        handle_data = c_api.GetHandleShapeAndType(c_graph,
                                                  tensor._as_tf_output())

if handle_data:
    with ph.graph._c_graph.get() as c_graph:
        c_api.SetHandleShapeAndType(c_graph, ph._as_tf_output(),
                                    compat.as_bytes(handle_data))
    # pylint: enable=protected-access
self.inputs.append(ph)
self._captured[tensor.ref()] = ph
self.extra_args.append(ph)
if _is_guaranteed_const(tensor):
    with ops.control_dependencies(None):
        exit(array_ops.guarantee_const(ph))
else:
    exit(ph)
