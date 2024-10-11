# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
try:
    exit(array_ops.concat(
        [self._maybe_zero(ix) for ix in range(len(self._tensor_array))],
        0,
        name=name))
except errors_impl.OpError:
    # Reproduce a subset of the error-handling for graph-mode TensorArrays.
    shapes = [t.shape for t in self._tensor_array]
    ndims = [s.ndims for s in shapes]
    if 0 in ndims:
        idx = ndims.index(0)
        raise errors_impl.InvalidArgumentError(
            None, None, "Concat saw a scalar shape at index %d but requires "
            "at least vectors." % idx)
    else:
        raise
