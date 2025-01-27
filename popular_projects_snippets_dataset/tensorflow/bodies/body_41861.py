# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Initializes an eager defined function.

    Args:
      name: str, the name for the created function.
      graph: Graph, the graph containing the operations in the function
      inputs: the tensors in the graph to be used as inputs to the function
      outputs: the tensors in the graph which will be outputs from the function
      attrs: dict mapping names of attributes to their AttrValue values
    """
for function_callback in _function_callbacks:
    function_callback(self, name, graph, tuple(inputs), tuple(outputs))

input_ops = set(arg.op for arg in inputs)
operations = [op for op in graph.get_operations() if op not in input_ops]

graph_output_names = graph._output_names  # pylint: disable=protected-access
if (graph_output_names is not None and
    all(ops.tensor_id(t) in graph_output_names for t in outputs)):
    output_names = [
        compat.as_bytes(graph_output_names[ops.tensor_id(t)]) for t in outputs
    ]
    if len(set(output_names)) != len(output_names):
        # There are duplicate names for some reason, probably an invalid
        # signature. Revert to auto-naming.
        output_names = []
else:
    output_names = []
with graph._c_graph.get() as c_graph:  # pylint: disable=protected-access
    fn = pywrap_tf_session.TF_GraphToFunction_wrapper(
        c_graph,
        compat.as_str(name),
        False,
        [o._c_op for o in operations],  # pylint: disable=protected-access
        [t._as_tf_output() for t in inputs],  # pylint: disable=protected-access
        [t._as_tf_output() for t in outputs],  # pylint: disable=protected-access
        output_names,
        [o._c_op for o in graph.control_outputs],  # pylint: disable=protected-access
        [],  # control_output_names
        None,
        compat.as_str(""))

self._c_func = c_api_util.ScopedTFFunction(fn, name)

for name, attr_value in attrs.items():
    serialized = attr_value.SerializeToString()
    # TODO(iga): this creates and deletes a new TF_Status for every attr.
    # It might be worth creating a convenient way to re-use status.
    pywrap_tf_session.TF_FunctionSetAttrValueProto(fn, compat.as_str(name),
                                                   serialized)

# NOTE(feyu): Do not cache signature and definition at initialization to
# save memory usage of concrete functions never called through Python. We
# cache them on the first call of .definition and .signature.
signature = self._get_definition().signature

self._name = compat.as_bytes(signature.name)
with ops.init_scope():
    if context.executing_eagerly():
        context.ensure_initialized()
        context.add_function(fn)
        self._function_deleter = _EagerDefinedFunctionDeleter(self.name)
        self._registered_on_context = True

self._num_outputs = len(signature.output_arg)
self._output_types = [o.type for o in signature.output_arg]
self._output_shapes = [o.shape for o in outputs]
self._control_captures = graph.control_captures
# Shallow copy outputs since ConcreteFunction may mutate it.
self._func_graph_outputs = list(outputs)
self.grad_func_name = None
self.python_grad_func = None
self._grad_func = None
self.graph = graph
self._stateful_ops = tuple(op for op in operations if op._is_stateful)  # pylint: disable=protected-access
