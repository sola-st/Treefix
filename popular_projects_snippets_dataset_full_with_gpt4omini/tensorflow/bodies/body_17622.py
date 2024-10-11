# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Implementation of gradients()."""
if context.executing_eagerly():
    raise RuntimeError("tf.gradients is not supported when eager execution "
                       "is enabled. Use tf.GradientTape instead.")
ys = variable_utils.convert_variables_to_tensors(_AsList(ys))
xs = [
    x.handle if resource_variable_ops.is_resource_variable(x) else x
    for x in _AsList(xs)
]
if grad_ys is not None:
    grad_ys = _AsList(grad_ys)

# Handle CompositeTensors.
if (any(isinstance(x, composite_tensor.CompositeTensor) for x in xs) or
    any(isinstance(y, composite_tensor.CompositeTensor) for y in ys)):
    flat_xs = composite_tensor_gradient.get_flat_tensors_for_gradients(xs)
    flat_ys = composite_tensor_gradient.get_flat_tensors_for_gradients(ys)
    flat_grad_ys = (
        None if grad_ys is None else
        composite_tensor_gradient.get_flat_tensors_for_gradients(grad_ys))
    flat_grads = _GradientsHelper(flat_ys, flat_xs, flat_grad_ys, name,
                                  colocate_gradients_with_ops, gate_gradients,
                                  aggregation_method, stop_gradients,
                                  unconnected_gradients, src_graph)
    exit(composite_tensor_gradient.replace_flat_tensors_for_gradients(
        xs, flat_grads))

if src_graph is None:
    src_graph = ops.get_default_graph()
try:
    unconnected_gradients = UnconnectedGradients(unconnected_gradients)
except ValueError:
    raise ValueError(
        f"Unknown value for unconnected_gradients: '{unconnected_gradients}'")

# If src_graph is a _FuncGraph (i.e. a function body), gather it and all
# ancestor graphs. This is necessary for correctly handling captured values.
func_graphs = []
curr_graph = src_graph
while _IsFunction(curr_graph):
    func_graphs.append(curr_graph)
    if isinstance(curr_graph, FuncGraph):
        curr_graph = curr_graph.outer_graph
    else:
        assert isinstance(curr_graph, framework_function._FuncGraph)  # pylint: disable=protected-access
        curr_graph = curr_graph._outer_graph  # pylint: disable=protected-access

stop_gradients = [] if stop_gradients is None else _AsList(stop_gradients)
if grad_ys is None:
    grad_ys = [None] * len(ys)

with ops.name_scope(
    name, "gradients",
    list(ys) + list(xs) + list(stop_gradients) + list(grad_ys)) as grad_scope:
    # Get a uid for this call to gradients that can be used to help
    # cluster ops for compilation.
    gradient_uid = ops.get_default_graph().unique_name("uid")
    ys = ops.convert_n_to_tensor_or_indexed_slices(ys, name="y")
    xs = ops.internal_convert_n_to_tensor_or_indexed_slices(
        xs, name="x", as_ref=True)
    xs_set = object_identity.ObjectIdentitySet(xs)
    grad_ys = _DefaultGradYs(grad_ys, ys, colocate_gradients_with_ops,
                             gradient_uid)

    # The approach we take here is as follows: Create a list of all ops in the
    # subgraph between the ys and xs.  Visit these ops in reverse order of ids
    # to ensure that when we visit an op the gradients w.r.t its outputs have
    # been collected.  Then aggregate these gradients if needed, call the op's
    # gradient function, and add the generated gradients to the gradients for
    # its input.

    # Initialize the pending count for ops in the connected subgraph from ys
    # to the xs.
    to_ops = [t.op for t in ys]
    from_ops = [t.op for t in xs]
    stop_gradient_ops = [t.op for t in stop_gradients]
    reachable_to_ops, pending_count, loop_state = _PendingCount(
        to_ops, from_ops, colocate_gradients_with_ops, func_graphs, xs_set)

    # Iterate over the collected ops.
    #
    # grads: op => list of gradients received on each output endpoint of the
    # op.  The gradients for each endpoint are initially collected as a list.
    # When it is time to call the op's gradient function, for each endpoint we
    # aggregate the list of received gradients into a Add() Operation if there
    # is more than one.
    grads = {}

    # Add the initial gradients for the ys.
    for y, grad_y in zip(ys, grad_ys):
        _SetGrad(grads, y, grad_y)

    # Initialize queue with to_ops.
    queue = collections.deque()
    # Add the ops in 'to_ops' into the queue.
    to_ops_set = set()
    for op in to_ops:
        # 'ready' handles the case where one output gradient relies on
        # another output's gradient.
        ready = (pending_count[op] == 0)
        if ready and op not in to_ops_set and op in reachable_to_ops:
            to_ops_set.add(op)
            queue.append(op)

    if loop_state:
        loop_exits = loop_state.ProcessUnusedLoopExits(pending_count, to_ops_set)
        for y in loop_exits:
            if backprop_util.IsTrainable(y):
                _SetGrad(grads, y, loop_state.ZerosLikeForExit(y))
                queue.append(y.op)

    stop_ops = _StopOps(from_ops, stop_gradient_ops, pending_count, xs_set)
    while queue:
        # generate gradient subgraph for op.
        op = queue.popleft()
        with _maybe_colocate_with(op, gradient_uid, colocate_gradients_with_ops):
            if loop_state:
                loop_state.EnterGradWhileContext(op, before=True)
            out_grads = _AggregatedGrads(grads, op, gradient_uid, loop_state,
                                         aggregation_method)
            if loop_state:
                loop_state.ExitGradWhileContext(op, before=True)

            grad_fn = None
            func_call = None
            is_partitioned_call = _IsPartitionedCall(op)
            # pylint: disable=protected-access
            is_func_call = (
                src_graph._is_function(op.type) or is_partitioned_call)
            # pylint: enable=protected-access
            has_out_grads = any(isinstance(g, ops.Tensor) or g for g in out_grads)
            if has_out_grads and (op not in stop_ops):
                try:
                    grad_fn = ops.get_gradient_function(op)
                except LookupError:
                    if is_func_call:
                        if is_partitioned_call:
                            func_name = compat.as_bytes(op.get_attr("f").name)
                            func_call = src_graph._get_function(  # pylint: disable=protected-access
                                func_name)
                            # When a graph is imported, the FunctionDefs are not copied over
                            # to each sub-graph so we recursively search the outer graphs
                            # for the FunctionDef.
                            if not func_call and hasattr(src_graph, "outer_graph"):
                                graph = src_graph.outer_graph
                                while graph is not None:
                                    func_call = graph._get_function(func_name)  # pylint: disable=protected-access
                                    if func_call  is not None:
                                        break
                                    if hasattr(graph, "outer_graph"):
                                        graph = graph.outer_graph
                                    else:
                                        break
                        else:
                            func_call = src_graph._get_function(op.type)  # pylint: disable=protected-access
                        # Note that __defun is not set if the graph is
                        # imported. If it's set, we prefer to access the original
                        # defun.
                        func_call = getattr(op, "__defun", func_call)
                        grad_fn = func_call.python_grad_func
                    else:
                        raise LookupError(
                            "No gradient defined for operation"
                            f"'{op.name}' (op type: {op.type}). "
                            "In general every operation must have an associated "
                            "`@tf.RegisterGradient` for correct autodiff, which this "
                            "op is lacking. If you want to pretend this "
                            "operation is a constant in your program, you may insert "
                            "`tf.stop_gradient`. This can be useful to silence the "
                            "error in cases where you know gradients are not needed, "
                            "e.g. the forward pass of tf.custom_gradient. "
                            "Please see more details in "
                            "https://www.tensorflow.org/api_docs/python/tf/custom_gradient.")  # pylint: disable=line-too-long
            if loop_state:
                loop_state.EnterGradWhileContext(op, before=False)

            # NOTE(skyewm): We don't support computing gradients wrt a loop variable
            # unless it's within the context of a single iteration (i.e. the
            # gradient is wrt to the loop parameter in the body function, not wrt or
            # through the initial value). This means if we're in a while loop
            # context, we should never see a switch node from this context.
            # pylint: disable=protected-access
            if (control_flow_util.IsSwitch(op) and
                op._control_flow_context is not None and
                op._control_flow_context.IsWhileContext() and
                op._control_flow_context ==
                ops.get_default_graph()._get_control_flow_context()):
                _RaiseNoGradWrtInitialLoopValError(op, from_ops, xs_set)
            # pylint: enable=protected-access

            if (grad_fn or is_func_call) and has_out_grads:
                # NOTE: If _AggregatedGrads didn't compute a value for the i'th
                # output, it means that the cost does not depend on output[i],
                # therefore dC/doutput[i] is 0.
                for i, out_grad in enumerate(out_grads):
                    if (not isinstance(out_grad, ops.Tensor) and not out_grad) and (
                        (not grad_fn and is_func_call)
                        or backprop_util.IsTrainable(op.outputs[i])):
                        # Only trainable outputs or outputs for a function call that
                        # will use SymbolicGradient get a zero gradient. Gradient
                        # functions should ignore the gradient for other outputs.
                        # TODO(apassos) gradients of resource handles might be an
                        # issue here because of zeros.
                        if loop_state:
                            out_grads[i] = loop_state.ZerosLikeV1WhileLoop(op, i)
                        elif default_gradient.supports_default_grad(op.outputs[i]):
                            # TODO(b/143286622): The supports_default_grad check is needed
                            # because While op emits non-differentiable resource tensors
                            # as outputs. Remove this check when that is not the case.
                            out_grads[i] = control_flow_state.ZerosLike(op, i)
                with ops.name_scope(op.name + "_grad"):
                    # pylint: disable=protected-access
                    with src_graph._original_op(op):
                        # pylint: enable=protected-access
                        if grad_fn:
                            # If grad_fn was found, do not use SymbolicGradient even for
                            # functions.
                            in_grads = _MaybeCompile(grad_scope, op, func_call,
                                                     lambda: grad_fn(op, *out_grads))
                        else:
                            # For function call ops, we add a 'SymbolicGradient'
                            # node to the graph to compute gradients.
                            in_grads = _MaybeCompile(grad_scope, op, func_call,
                                                     lambda: _SymGrad(op, out_grads))
                        in_grads = _AsList(in_grads)
                        _VerifyGeneratedGradients(in_grads, op)
                        if gate_gradients and len([x for x in in_grads
                                                   if x is not None]) > 1:
                            with ops.device(None):
                                with ops._colocate_with_for_gradient(  # pylint: disable=protected-access
                                    None,
                                    gradient_uid,
                                    ignore_existing=True):
                                    in_grads = control_flow_ops.tuple(in_grads)
                _LogOpGradients(op, out_grads, in_grads)
            else:
                # If no grad_fn is defined or none of out_grads is available,
                # just propagate a list of None backwards.
                in_grads = [None] * len(_Inputs(op, xs_set))
            # Note: we don't filter out eager inputs here because the inputs need to
            # line up with in_grads.
            for i, (t_in, in_grad) in enumerate(zip(_Inputs(op, xs_set), in_grads)):
                if in_grad is not None:
                    if (isinstance(in_grad, ops.Tensor) and
                        t_in.dtype != dtypes.resource):
                        try:
                            in_grad.set_shape(t_in.get_shape())
                        except ValueError:
                            raise ValueError(
                                "Incompatible shapes between op input and calculated "
                                f"input gradient. Forward operation: {op.name}. Input "
                                f"index: {i}. Original input shape: {t_in.shape}. "
                                f"Calculated input gradient shape: {in_grad.shape}")
                    if not isinstance(t_in, ops.EagerTensor):
                        _SetGrad(grads, t_in, in_grad)
            if loop_state:
                loop_state.ExitGradWhileContext(op, before=False)

      # Update pending count for the inputs of op and enqueue ready ops.
        _UpdatePendingAndEnqueueReady(grads, op, queue, pending_count, loop_state,
                                      xs_set)

if loop_state:
    loop_state.PostProcessing()
exit([_GetGrad(grads, x, unconnected_gradients) for x in xs])
