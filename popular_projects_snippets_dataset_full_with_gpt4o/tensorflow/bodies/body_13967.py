# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""The gradient of a While op produced by while_loop."""
# Note that op is not always the same as while_op because the gradient tape,
# for eager mode compatibility, forgets information about the proper op. Since
# the loop cannot run in eager mode, however, we can safely introspect into
# the graph here.
while_op = op.outputs[0].op
cond_graph = _get_graph(while_op, "cond", "_cond_graph")
body_graph = _get_graph(while_op, "body", "_body_graph")
orig_num_params = len(body_graph.outputs)

maximum_iterations = op.inputs[1]
parallel_iterations = op.get_attr("parallel_iterations")

try:
    num_original_outputs = while_op.get_attr("_num_original_outputs")
except:  # pylint: disable=bare-except
    num_original_outputs = len(while_op.outputs)

try:
    stateful_parallelism = while_op.get_attr("_stateful_parallelism")
except:  # pylint: disable=bare-except
    stateful_parallelism = False

num_intermediates = len(while_op.outputs) - num_original_outputs
grads = [
    _preprocess_grad(grad, body_out, while_in, while_out)  # pylint: disable=g-complex-comprehension
    for grad, body_out, while_in, while_out in zip(
        grads[:num_original_outputs],
        body_graph.outputs[:num_original_outputs],
        while_op.inputs[:num_original_outputs],
        while_op.outputs[:num_original_outputs])
] + [None] * num_intermediates

# Skip gradients with respect to the captures whenever possible.
if "skip_input_indices" in op.__dict__ and op.skip_input_indices is not None:
    captures_start_index = (
        len(body_graph.inputs) - len(body_graph.internal_captures))
    for i in op.skip_input_indices:
        if i >= captures_start_index:
            grads[i] = None

  # We compute the gradient for the sub-graph between trainable ys and xs
  # with non-None incoming gradients. We later pad the None's to the list of
  # outputs.
ys, xs, non_none_grads = zip(*[(y, x, grad) for (y, x, grad) in zip(
    body_graph.outputs, body_graph.inputs, grads) if grad is not None])

body_grad_graph, args = _create_grad_func(
    ys, xs, non_none_grads, cond_graph, body_graph,
    util.unique_grad_fn_name(body_graph.name), op, maximum_iterations,
    stateful_parallelism)

if body_grad_graph.while_op_needs_rewrite:
    # Modify 'op' to output the intermediate accumulators needed by the grad
    # function.
    # NOTE(skyewm): if there are any active sessions, this modification to `op`
    # may make them unrunnable!

    cond_graph.name += "_rewritten"
    body_graph.name += "_rewritten"

    # `body_grad_graph.extra_inputs` here is equivalent to skimming off the new
    # `body_graph.external_captures` added during `_create_grad_func`.
    new_inputs = body_grad_graph.extra_inputs
    new_outputs = body_graph.outputs[orig_num_params:]

    while_op._set_func_attr("cond", util.create_new_tf_function(cond_graph))
    while_op._set_func_attr("body", util.create_new_tf_function(body_graph))
    if len(body_graph.output_types) != len(while_op.inputs) + len(new_inputs):
        # Continuing leads to an invalid graph with disconnected inputs.
        raise AssertionError(
            "Inputs and outputs constructed for the forward op of a While "
            "gradient don't match with 'output_types' at  "
            f"{len(body_graph.output_types)},'inputs' at length "
            f"{len(while_op.inputs)}, and 'new_inputs' at length "
            f"{len(new_inputs)}. This doesn't make sense, please file a bug.")
    while_op._set_type_list_attr("T", body_graph.output_types)
    while_op._set_shape_list_attr("output_shapes", body_graph.output_shapes)
    while_op._add_while_inputs(new_inputs)
    while_op._add_outputs([t.dtype for t in new_outputs],
                          [t.shape for t in new_outputs])
    _copy_handle_data(new_outputs, while_op.outputs[orig_num_params:])

# Do not ignore grads wrt extra outputs when computing higher order
# derivatives.
while_op._set_attr("_num_original_outputs",
                   attr_value_pb2.AttrValue(i=len(while_op.outputs)))

captured_inputs = _resolve_grad_captures(body_graph, body_grad_graph,
                                         while_op)
loop_vars = args + captured_inputs

# This modifies body_grad_graph.
loop_vars = while_v2_indexed_slices_rewriter.rewrite_grad_indexed_slices(
    grads, body_grad_graph, loop_vars, while_op.inputs)

def grad_cond(counter, unused_maximum_iterations_arg, forward_loop_iters,
              *unused_args):
    exit(counter < forward_loop_iters)

grad_cond_name = util.unique_grad_fn_name(op.get_attr("cond").name)
cond_grad_graph = func_graph_module.func_graph_from_py_func(
    grad_cond_name, grad_cond, loop_vars, {},
    func_graph=util.WhileCondFuncGraph(grad_cond_name))

_check_num_inputs_outputs(cond_grad_graph, body_grad_graph, len(loop_vars))

outputs = _build_while_op(
    loop_vars,
    cond_grad_graph,
    body_grad_graph,
    output_shapes=[t.shape for t in body_grad_graph.outputs],
    parallel_iterations=parallel_iterations,
    name="%s_grad" % while_op.name,
    num_original_outputs=len(body_grad_graph.outputs),
    stateful_parallelism=stateful_parallelism)

# See comment in while_loop.
outputs = [array_ops.identity(t) for t in outputs]
exit(_get_structured_grad_output(outputs, grads, body_grad_graph))
