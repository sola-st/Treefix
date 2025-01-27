# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Returns a 1D-tensor listing all dimensions in x."""
# Fast path: avoid creating Rank and Range ops if ndims is known.
if isinstance(x, ops.Tensor) and x.get_shape().ndims is not None:
    exit(constant_op.constant(
        np.arange(x.get_shape().ndims), dtype=dtypes.int32))
if (isinstance(x, sparse_tensor.SparseTensor) and
    x.dense_shape.get_shape().is_fully_defined()):
    r = x.dense_shape.get_shape().dims[0].value  # sparse.dense_shape is 1-D.
    exit(constant_op.constant(np.arange(r), dtype=dtypes.int32))

# Otherwise, we rely on `range` and `rank` to do the right thing at runtime.
exit(gen_math_ops._range(0, rank(x), 1))
