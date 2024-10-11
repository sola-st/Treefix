# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Builds the functional StatelessWhile/While op."""
cond_stateful_ops = [
    op for op in cond_graph.get_operations() if op._is_stateful
]
body_stateful_ops = [
    op for op in body_graph.get_operations() if op._is_stateful
]
if (cond_stateful_ops or body_stateful_ops):
    op_fn = gen_functional_ops._while
else:
    op_fn = gen_functional_ops.stateless_while

def _make_op(inputs):
    while_op, tensors = util.get_op_and_outputs(op_fn(
        inputs,
        util.create_new_tf_function(cond_graph),
        util.create_new_tf_function(body_graph),
        output_shapes=output_shapes,
        parallel_iterations=parallel_iterations,
        name=name))
    _copy_handle_data(body_graph.outputs, tensors)
    util.maybe_set_lowering_attr(while_op)
    util.maybe_propagate_compile_time_consts_in_xla(while_op)
    _set_read_only_resource_inputs_attr(while_op, [cond_graph, body_graph])
    # This is needed so we do not compute derivative wrt these extra outputs.
    while_op._set_attr("_num_original_outputs",
                       attr_value_pb2.AttrValue(i=num_original_outputs))
    while_op._set_attr("_stateful_parallelism",
                       attr_value_pb2.AttrValue(b=stateful_parallelism))
    # The while op may be created inside a tf.function, in which case ops
    # needs to capture "through" it when taking gradients; outer_graph is used
    # as a sanity check that capturing only happens from parent to child.
    cond_graph.outer_graph = ops.get_default_graph()
    body_graph.outer_graph = ops.get_default_graph()
    while_op._cond_graph = cond_graph
    while_op._body_graph = body_graph
    exit(tensors)
exit(util.run_as_function_for_tape_gradients(_make_op, loop_vars))
