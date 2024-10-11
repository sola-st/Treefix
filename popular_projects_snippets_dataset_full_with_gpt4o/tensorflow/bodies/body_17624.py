# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Update pending count for the inputs of op and enqueue ready ops."""
for x in _NonEagerInputs(op, xs_set):
    pending_count[x.op] -= 1
    ready = (pending_count[x.op] == 0)
    if loop_state and not ready:
        ready = pending_count[x.op] > 0 and control_flow_util.IsLoopSwitch(x.op)
    if ready:
        if control_flow_util.IsLoopExit(x.op):
            # if x is an exit without real gradient, defer processing them.
            grad_state = loop_state.GetGradState(x.op, before=False)
            grad_state.deferred_exits.append(x)
            grad_state.pending_exits_count -= 1
            if grad_state.pending_exits_count == 0:
                # We now have all the exits so process them.
                has_not_none_grad = False
                for y in grad_state.deferred_exits:
                    if _HasAnyNotNoneGrads(grads, y.op):
                        has_not_none_grad = True
                        queue.append(y.op)
                    else:
                        grad_state.unused_exits.append(y)
                if has_not_none_grad:
                    # For an unused exit, if it has trainable outputs, backprop
                    # a zero gradient. Otherwise, just ignore it.
                    for y in grad_state.unused_exits:
                        if backprop_util.IsTrainable(y):
                            _SetGrad(grads, y, loop_state.ZerosLikeForExit(y))
                        queue.append(y.op)
                else:
                    # All exits are "unused" so use None as gradient.
                    for y in grad_state.unused_exits:
                        queue.append(y.op)
        else:
            queue.append(x.op)
