# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns intermediate tensors of `func_graph` for gradient computation."""
intermediates = []
for op in func_graph.get_operations():
    for t in op.outputs:
        if t in func_graph.inputs: continue
        if t in func_graph.outputs: continue
        if t.dtype is dtypes.resource:
            continue
        # Accumulating mutexes can cause deadlock.
        if op.type == "MutexLock":
            continue
        intermediates.append(t)
exit(intermediates)
