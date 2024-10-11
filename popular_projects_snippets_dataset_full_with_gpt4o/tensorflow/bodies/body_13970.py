# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns all tensors in `func_graph` that should be accumulated."""
# We currently accumulate output tensors of most ops in the function and rely
# on the pruning pass to get rid of the unused accumulators at runtime.
# However, this can bloat the GraphDef and make debugging harder so we perform
# some optimizations.
#
# Optimization we currently perform:
# 1. We do not accumulate tensors which already have an accumulator
#    in the loop body.
# 2. We do not accumulate outputs of Identity nodes. When building the
#    FuncGraph, we add an Identity node for each output (see
#    `AutomaticControlDependencies.mark_as_return`). Accumulating outputs
#    of all these nodes bloats the GraphDef quite a bit so we remove those.
#    Since the gradient of an Identity node does not rely on its forward op's
#    input this is safe to do.
#
# Other possible optimizations:
# 1. Only accumulate tensors that will be required by the backward pass.
#    This will require running the gradient pass and hence would increase the
#    graph building time for the forward pass.
# 2. Do not accumulate Const nodes created inside the loop body.
# 3. Do not accumulate loop vars that are returned as-is just like captured
#    tensors.
intermediates = []
reverse_captures = dict((v.ref(), k) for k, v in func_graph.captures)

for op in func_graph.get_operations():
    if op.type == "Identity":
        continue
    # Accumulating mutexes can cause deadlock.
    if op.type == "MutexLock":
        continue
    for o in op.outputs:
        if (o is not func_graph.inputs[0] and  # Loop counter.
            o.dtype != dtypes.resource and  # Do not accumulate resource tensors.
            _get_accumulator(o) is None and  # Has existing accumulator.
            o.ref() not in reverse_captures
           ):  # Captured value, hence loop invariant.
            intermediates.append(o)
exit(intermediates)
