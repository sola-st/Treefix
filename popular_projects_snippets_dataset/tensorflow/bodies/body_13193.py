# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""The gradient of an If op produced by cond_v2."""
# Get the if operator (this logic handles the case where op is a MockOp)
if_op = op.outputs[0].op
true_graph, false_graph = get_func_graphs(if_op)
# Note: op.graph != ops.get_default_graph() when we are computing the gradient
# of a nested cond.
assert true_graph.outer_graph == if_op.graph
assert false_graph.outer_graph == if_op.graph

# Create grad functions that compute the gradient of the true/false forward
# graphs. These functions will capture tensors from the forward pass
# functions.
true_grad_graph = _create_grad_func(
    true_graph, grads, util.unique_grad_fn_name(true_graph.name))
false_grad_graph = _create_grad_func(
    false_graph, grads, util.unique_grad_fn_name(false_graph.name))

# Replaces output None grads with zeros if at least one branch has non-None
# grad at that index.
_create_zeros_for_none_grads([true_graph, false_graph],
                             [true_grad_graph, false_grad_graph])

if (true_grad_graph.op_needs_rewrite or false_grad_graph.op_needs_rewrite):
    # Modify 'op' to output the intermediates needed by the grad functions. Note
    # that all needed intermediates are wrapped in optionals. Each optional
    # intermediate output will have a value iff its corresponding branch is
    # taken.
    # NOTE(skyewm): if there are any active sessions, this modification to `op`
    # may make them unrunnable!

    if control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()):
        # XLA does not yet support optionals, so output intermediates directly and
        # make them match via FakeParams, which can be converted to zeros in XLA.
        # TODO(skyewm,jpienaar): can XLA support optionals?
        true_intermediates = true_grad_graph.xla_intermediates
        false_intermediates = false_grad_graph.xla_intermediates
        extra_true_outputs, extra_false_outputs = _make_intermediates_match_xla(
            [true_graph, false_graph], [true_intermediates, false_intermediates])
    else:
        true_intermediates = true_grad_graph.wrapped_intermediates
        false_intermediates = false_grad_graph.wrapped_intermediates
        # Make outputs match by adding none optionals.
        extra_true_outputs, extra_false_outputs = _make_intermediates_match(
            [true_graph, false_graph], [true_intermediates, false_intermediates])

    true_graph.outputs.extend(extra_true_outputs)
    false_graph.outputs.extend(extra_false_outputs)
    # TODO(skyewm): indicate it's an internal bug if this fails.
    _check_same_outputs(_COND, [true_graph, false_graph])

    true_graph.name += "_rewritten"
    false_graph.name += "_rewritten"

    if_op._set_func_attr("then_branch", util.create_new_tf_function(true_graph))
    if_op._set_func_attr("else_branch",
                         util.create_new_tf_function(false_graph))
    if_op._set_type_list_attr("Tout", true_graph.output_types)
    if_op._set_shape_list_attr("output_shapes", true_graph.output_shapes)
    if_op._add_outputs(
        [t.dtype for t in extra_true_outputs],
        [t.shape for t in extra_true_outputs])

# Resolve references to forward graph tensors in grad graphs and ensure
# they are in-scope, i.e., belong to one of outer graphs of the grad graph.
true_grad_inputs = _resolve_grad_inputs(true_graph, true_grad_graph)
false_grad_inputs = _resolve_grad_inputs(false_graph, false_grad_graph)

# This modifies true_grad_graph and false_grad_graph.
_make_output_composite_tensors_match(_COND,
                                     [true_grad_graph, false_grad_graph])

outputs = _build_cond(
    if_op.inputs[0],
    true_grad_graph,
    false_grad_graph,
    true_grad_inputs,
    false_grad_inputs,
    building_gradient=True,
)

# The predicate has no gradient.
exit([None] + outputs)
