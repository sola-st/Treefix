# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""The gradient of a Case op produced by tf.switch_case."""
# Get the Case operator (this logic handles the case where op is a MockOp)
case_op = op.outputs[0].op
branch_graphs = get_func_graphs(case_op)
assert branch_graphs
# Note: op.graph != ops.get_default_graph() when we are computing the gradient
# of a nested cond.
for branch_graph in branch_graphs:
    assert branch_graph.outer_graph == case_op.graph

# Create grad functions that compute the gradient of the branch forward
# graphs. These functions will capture tensors from the forward pass
# functions.
branch_grad_graphs = []
for branch_graph in branch_graphs:
    branch_grad_graphs.append(
        _create_grad_func(branch_graph, grads,
                          util.unique_grad_fn_name(branch_graph.name)))
# Replaces output None grads with zeros if at least one branch has non-None
# grad at that index.
_create_zeros_for_none_grads(branch_graphs, branch_grad_graphs)

if any(g.op_needs_rewrite for g in branch_grad_graphs):
    # Modify 'op' to output the intermediates needed by the grad functions. Note
    # that all needed intermediates are wrapped in optionals. Each optional
    # intermediate output will have a value iff its corresponding branch is
    # taken.
    # NOTE(bjp): if there are any active sessions, this modification to `op`
    # may make them unrunnable!

    if control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()):
        # XLA does not yet support optionals, so output intermediates directly and
        # make them match via FakeParams, which can be converted to zeros in XLA.
        # TODO(bjp,jpienaar): can XLA support optionals?
        branches_intermediates = [
            branch_grad_graph.xla_intermediates
            for branch_grad_graph in branch_grad_graphs
        ]
        extra_branch_outputs = _make_intermediates_match_xla(
            branch_graphs, branches_intermediates)
    else:
        branch_intermediates = [
            g.wrapped_intermediates for g in branch_grad_graphs
        ]
        # Make outputs match by adding none optionals.
        extra_branch_outputs = _make_intermediates_match(branch_graphs,
                                                         branch_intermediates)

    for branch_graph, extra_outputs in zip(branch_graphs, extra_branch_outputs):
        branch_graph.outputs.extend(extra_outputs)
    # TODO(bjp): indicate it's an internal bug if this fails.
    _check_same_outputs(_CASE, branch_graphs)

    for branch_graph in branch_graphs:
        branch_graph.name += "_rewritten"

    case_op._set_func_list_attr("branches", [
        util.create_new_tf_function(branch_graph)
        for branch_graph in branch_graphs
    ])
    case_op._set_type_list_attr("Tout", branch_graphs[0].output_types)
    case_op._set_shape_list_attr("output_shapes",
                                 branch_graphs[0].output_shapes)
    case_op._add_outputs([t.dtype for t in extra_branch_outputs[0]],
                         [t.shape for t in extra_branch_outputs[0]])

# Resolve references to forward graph tensors in grad graphs and ensure
# they are in-scope, i.e., belong to one of outer graphs of the grad graph.
branches_grad_inputs = [
    _resolve_grad_inputs(branch_graph, branch_grad_graph) for branch_graph,
    branch_grad_graph in zip(branch_graphs, branch_grad_graphs)
]

# This modifies the graphs in branch_grad_graphs.
_make_output_composite_tensors_match(_CASE, branch_grad_graphs)

try:
    lowering = case_op._get_attr_bool("_lower_using_switch_merge")
except errors_impl.NotFoundError:
    lowering = None

outputs = _build_case(
    case_op.inputs[0],
    branch_grad_graphs,
    branches_grad_inputs,
    name="gradient",
    lower_using_switch_merge=lowering)

# The predicate has no gradient.
exit([None] + outputs)
