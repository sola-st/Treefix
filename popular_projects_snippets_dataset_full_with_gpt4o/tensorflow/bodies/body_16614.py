# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
# The grad loop state for the outer while loop.
self._outer_grad_state = None

# The while loop context for forward.
self._forward_context = None

# The loop counter added by AddForwardLoopCounter. It is the value
# of the loop counter for the next iteration.
self._forward_index = None

# A sync op for forward.
self._forward_sync = None

# The while loop context for backprop.
self._grad_context = None

# The loop counter added by AddBackpropLoopCounter. It is the value
# of the loop counter for the current iteration.
self._grad_index = None

# A sync op for backprop.
self._grad_sync = None

# Information needed by backprop.
self._history_map = {}
self._switch_map = {}
self._unused_exits = []
self._deferred_exits = []
self._forward_loop_exits = list(forward_ctxt.loop_exits)
self._pending_exits_count = len(forward_ctxt.loop_exits)

self._outer_grad_state = outer_grad_state
if outer_grad_state:
    outer_forward_ctxt = outer_grad_state.forward_context
else:
    if not hasattr(forward_ctxt, "outer_context"):
        raise ValueError("Failed to call gradients on a while loop without"
                         "properly serializing graph via MetaGraphDef")
    outer_forward_ctxt = forward_ctxt.outer_context

# Add the forward loop counter.
with forward_ctxt._graph.as_default():  # pylint: disable=protected-access
    if outer_forward_ctxt:
        outer_forward_ctxt.Enter()
    cnt, forward_index = forward_ctxt.AddForwardLoopCounter(outer_grad_state)
    if outer_forward_ctxt:
        outer_forward_ctxt.Exit()
self._forward_context = forward_ctxt
self._forward_index = forward_index

# Add the backprop WhileContext, and the backprop loop counter.
if outer_grad_state:
    # This is a nested loop. Remember the iteration counts for each
    # execution of this inner loop.
    outer_forward_ctxt.AddName(cnt.name)
    history_cnt = outer_grad_state.AddForwardAccumulator(cnt)

    outer_grad_ctxt = outer_grad_state.grad_context
    outer_grad_ctxt.Enter()
    self._grad_context = control_flow_ops.WhileContext(
        maximum_iterations=forward_ctxt.maximum_iterations,
        parallel_iterations=forward_ctxt.parallel_iterations,
        back_prop=forward_ctxt.back_prop,
        swap_memory=forward_ctxt.swap_memory,
        name=forward_ctxt.name,
        grad_state=self)
    real_cnt = outer_grad_state.AddBackpropAccumulatedValue(history_cnt, cnt)
    self._grad_index = self._grad_context.AddBackpropLoopCounter(
        real_cnt, outer_grad_state)
    outer_grad_ctxt.Exit()
else:
    if outer_forward_ctxt:
        outer_forward_ctxt.Enter()
    self._grad_context = control_flow_ops.WhileContext(
        maximum_iterations=forward_ctxt.maximum_iterations,
        parallel_iterations=forward_ctxt.parallel_iterations,
        back_prop=forward_ctxt.back_prop,
        swap_memory=forward_ctxt.swap_memory,
        name=forward_ctxt.name,
        grad_state=self)
    self._grad_index = self._grad_context.AddBackpropLoopCounter(
        cnt, outer_grad_state)
    if outer_forward_ctxt:
        outer_forward_ctxt.Exit()
