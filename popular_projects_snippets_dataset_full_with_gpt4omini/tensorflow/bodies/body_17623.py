# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Return true iff op has real gradient."""
out_grads = _GetGrads(grads, op)
for out_grad in out_grads:
    if isinstance(out_grad, (ops.Tensor, indexed_slices.IndexedSlices)):
        exit(True)
    if out_grad and isinstance(out_grad, collections_abc.Sequence):
        if any(g is not None for g in out_grad):
            exit(True)
exit(False)
