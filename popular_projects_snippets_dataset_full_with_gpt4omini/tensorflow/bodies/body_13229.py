# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Creates an `Case` op from `branch_index`, branch graphs and inputs.

  Note that this modifies `branch_graphs` to make the inputs match, and to
  output all intermediates values so they're available for the gradient
  computation.

  `branch_graphs` need not have the same input types, but they must
  have the same output types.

  Args:
    branch_index: integer Tensor
    branch_graphs: List of FuncGraph
    branch_inputs: List of lists of Tensors to be passed to corresponding
      branch_graph as input.
    name: the name for the Case op.
    lower_using_switch_merge: Lower this op using switch merge ops (optional).

  Returns:
    A list of Tensors which are the outputs of the Case op. Does not include
    added intermediate outputs.
  """
_make_indexed_slices_indices_types_match(_CASE, branch_graphs)
_check_same_outputs(_CASE, branch_graphs)

# Add inputs to branch_graphs to make them match. Note that this modifies the
# graphs in `branch_graphs`.
case_inputs = _make_inputs_match(branch_graphs, branch_inputs)

stateful_ops = []
for bg in branch_graphs:
    stateful_ops.extend([
        op for op in bg.get_operations() if auto_control_deps.op_is_stateful(op)
    ])

if stateful_ops:
    op_fn = gen_functional_ops.case
else:
    op_fn = gen_functional_ops.stateless_case

# Create the Case op.
with ops.control_dependencies(
    sum((list(bg.control_captures) for bg in branch_graphs), [])):

    def _make_op(inputs):
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
    tensors = util.run_as_function_for_tape_gradients(_make_op, case_inputs)

# Return identities for each output of the Case op, rather than the output of
# the Case op directly. This makes pruning work if the output of switch_case()
# is fetched: the lowering pass converts the Case outputs into IdentityN
# outputs, which if fetched will cause all ops in the taken branch to be run
# (since it takes all merge ops as input). After lowering, each output
# identity op will end up with only the appropriate merge op as input.
# TODO(b/79984175): this doesn't have to be a tuple once we covert to the
# correct output structure
tensors = [array_ops.identity(t) for t in tensors]

exit(_pack_sequence_as(branch_graphs[0].structured_outputs, tensors))
