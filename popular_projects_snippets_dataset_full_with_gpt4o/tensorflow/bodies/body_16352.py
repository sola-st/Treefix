# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Generates and returns a FuncGraph for the given op and input_shapes."""
fdef = None
graph = op.graph
# Recursively search the func in graphs.
while graph is not None:
    func = graph._get_function(func_name)  # pylint: disable=protected-access
    if func is not None:
        fdef = func.definition
        break
    if hasattr(graph, "outer_graph"):
        graph = graph.outer_graph
    else:
        break

if fdef is None:
    raise KeyError("%s cannot be found in the graph" % func_name)

# `op.graph` may not be the same as `ops.get_default_graph()` e.g.
# in the case of nested if ops or when the gradient is being computed
# from inside a Defun. We build the `func_graph` with `op.graph` as its
# `outer_graph`. This resembles how the `FuncGraph` was built in the
# forward pass. We need this so that we can resolve references to tensors
# in `func_graph` from its gradient graph in `_resolve_grad_inputs`.
with op.graph.as_default():
    func_graph = function_def_to_graph.function_def_to_graph(
        fdef, input_shapes=input_shapes)

# TODO(xjun): Ideally we want to retrieve the gradient functions instead of
# re-create them. But the lifetime of gradient functions of PartitionedCall
# ops is attached to ParitionedCall ops in the original func_graph and
# when we are inside this function we don't have access to the original
# func_graph or PartitionedCall ops. See cl/499362867 and cl/273858076 for
# more context.
for operation in func_graph.get_operations():
    if operation.type in ["PartitionedCall", "StatefulPartitionedCall"]:
        f = graph._get_function(operation.get_attr("f").name)  # pylint: disable=protected-access
        try:
            cf = function.ConcreteFunction(f.graph, attrs=f.definition.attr)
        except AttributeError:
            # f is not found or f is a _DefinedFunction that doesn't have a graph.
            continue
        operation._gradient_function = cf._get_gradient_function()  # pylint: disable=protected-access

exit(func_graph)
