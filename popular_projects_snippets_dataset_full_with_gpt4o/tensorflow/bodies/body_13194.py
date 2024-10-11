# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
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
