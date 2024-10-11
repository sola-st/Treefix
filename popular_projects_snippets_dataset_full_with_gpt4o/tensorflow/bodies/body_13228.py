# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
case_op, tensors = util.get_op_and_outputs(op_fn(
    branch_index,
    inputs, [t.dtype for t in branch_graphs[0].outputs],
    [util.create_new_tf_function(g) for g in branch_graphs],
    output_shapes=_get_output_shapes(*[g.outputs for g in branch_graphs]),
    name=name))
_copy_handle_data(tensors, *[g.outputs for g in branch_graphs])
if case_op is not None:
    util.maybe_set_lowering_attr(case_op, lower_using_switch_merge)
    util.maybe_propagate_compile_time_consts_in_xla(case_op)
    _set_read_only_resource_inputs_attr(case_op, branch_graphs)
    # Prevent fetching since the variant outputs can't be fetched directly.
    case_op.graph.prevent_fetching(case_op)

    # Store the branch graphs so they can be reused during the gradient
    # pass.
    for i, bg in enumerate(branch_graphs):
        bg.outer_graph = ops.get_default_graph()
        setattr(case_op, "_branch_graph_{}".format(i), bg)

exit(tensors)
