# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Creates an If op from the specified predicate, branch functions and inputs.

  Note that this modifies true_graph and false_graph to make the inputs match,
  and to output all intermediates values so they're available for the gradient
  computation.

  true_graph and false_graph need not have the same input types, but they must
  have the same output types.

  Args:
    pred: boolean Tensor
    true_graph: FuncGraph
    false_graph: FuncGraph
    true_inputs: a list of Tensors to be passed to true_graph as input.
    false_inputs: a list of Tensors to be passed to false_graph as input.
    building_gradient: Whether this is a gradient If op.
    name: the name for the If op.

  Returns:
    A list of Tensors which are the outputs of the If op. Does not include added
    intermediate outputs.
  """
_make_indexed_slices_indices_types_match(_COND, [true_graph, false_graph])
_check_same_outputs(_COND, [true_graph, false_graph])

# Add inputs to true_graph and false_graph to make them match. Note that
# this modifies true_graph and false_graph.
cond_inputs = _make_inputs_match([true_graph, false_graph],
                                 [true_inputs, false_inputs])
# We do not output intermediates of the gradient If op since this is just
# for backwards compatibility with existing code.
if not building_gradient and util.output_all_intermediates():
    # Add all intermediate tensors as function outputs so they're available for
    # the gradient computation. Since the outputs of the two functions must
    # match, we wrap all the intermediates in optionals. Each intermediate
    # output will have a value iff its corresponding branch is taken.

    true_intermediates = _get_intermediates(true_graph)
    false_intermediates = _get_intermediates(false_graph)

    # Wrap intermediates in optionals.
    wrapped_true_intermediates = _wrap_intermediates(true_graph,
                                                     true_intermediates)
    wrapped_false_intermediates = _wrap_intermediates(false_graph,
                                                      false_intermediates)

    # Make outputs match by adding none optionals.
    extra_true_outputs, extra_false_outputs = _make_intermediates_match(  # pylint: disable=unbalanced-tuple-unpacking
        [true_graph, false_graph],
        [wrapped_true_intermediates, wrapped_false_intermediates])

    true_graph.outputs.extend(extra_true_outputs)
    false_graph.outputs.extend(extra_false_outputs)
    _check_same_outputs(_COND, [true_graph, false_graph])

# Create the If op.
with ops.control_dependencies(
    list(true_graph.control_captures) + list(false_graph.control_captures)):
    true_stateful_ops = [
        op for op in true_graph.get_operations() if op._is_stateful
    ]
    false_stateful_ops = [
        op for op in false_graph.get_operations() if op._is_stateful
    ]
    if (true_stateful_ops or false_stateful_ops):
        op_fn = gen_functional_ops._if
    else:
        op_fn = gen_functional_ops.stateless_if

    def _make_op(inputs):
        if_op, tensors = util.get_op_and_outputs(op_fn(
            pred,
            inputs, [t.dtype for t in true_graph.outputs],
            util.create_new_tf_function(true_graph),
            util.create_new_tf_function(false_graph),
            output_shapes=_get_output_shapes(true_graph.outputs,
                                             false_graph.outputs),
            name=name))
        _copy_handle_data(tensors, true_graph.outputs, false_graph.outputs)
        # `if_op` is None if this is a `StatelessIf` op with no outputs.
        if if_op is not None:
            # The true and false graphs have already been created, and we need that
            # to happen before we know which tensors will be captured and so whether
            # to wrap the cond in a tf.function. Post-hoc mutation of the branch
            # `outer_graph` properties seems like the only option if we want to
            # conditionally wrap in a function.
            true_graph.outer_graph = ops.get_default_graph()
            false_graph.outer_graph = ops.get_default_graph()
            if_op._true_graph = true_graph
            if_op._false_graph = false_graph
            util.maybe_set_lowering_attr(if_op)
            util.maybe_propagate_compile_time_consts_in_xla(if_op)
            _set_read_only_resource_inputs_attr(if_op, [true_graph, false_graph])
            # Prevent fetching since the variant outputs can't be fetched directly.
            if_op.graph.prevent_fetching(if_op)
        exit(tensors)
    tensors = util.run_as_function_for_tape_gradients(_make_op, cond_inputs)

# Return identities for each output of the If op, rather than the output of
# the If op directly. This makes pruning work if the output of cond() is
# fetched: the lowering pass converts the If outputs into IdentityN outputs,
# which if fetched will cause all ops in the taken branch to be run (since
# it takes all merge ops as input). After lowering, each output identity op
# will end up with only the appropriate merge op as input.
# TODO(b/79984175): this doesn't have to be a tuple once we covert to the
# correct output structure
tensors = [array_ops.identity(t) for t in tensors]

structured_output_specs = _get_compatible_structured_output_specs(true_graph,
                                                                  false_graph)
exit(_pack_sequence_as(structured_output_specs, tensors))
