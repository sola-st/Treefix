# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Multiplies batches of 2D matrices using map_fn.

  `output[n, i, k]` = sum_j (a[n, i, j] * b[n, j, k])` (for all `n`, `i`, `k`).

  Requires that `a[n, i].nrows()` == `b[n].nrows()` (for all `n` and `i`).

  Args:
    a: A 3D Tensor or RaggedTensor with `shape=[B, I, J]`, where dimensions `I`
      and `J` may be ragged.
    b: A 3D Tensor or RaggedTensor with `shape=[B, J, K]`, where dimensions `J`
      and `K` may be ragged.
    **kwargs: Additional arguments for `tf.matmul` (e.g. transpose_a).

  Returns:
    A 3D RaggedTensor with `shape=[B, (I), (K)]`.
  """
# Determine the ragged rank of the result.  In the normal case, we have:
#   [B, I, J] * [B, J, K] -> [B, I, K]
# Or if we're using transpose_b, then we have:
#   [B, I, J] * [B, K, J] -> [B, I, K]
# In either case, output_ragged_rank=2 iff the K dimension is ragged.
if (isinstance(b, ragged_tensor.RaggedTensor) and
    (b.ragged_rank == 2 or kwargs.get('transpose_b') or
     kwargs.get('adjoint_b'))):
    output_ragged_rank = 2
else:
    output_ragged_rank = 1

def single_batch_matmul(x):
    out = _matmul_2d(x[0], x[1], **kwargs)
    if output_ragged_rank == 2:
        out = ragged_tensor.RaggedTensor.from_tensor(out)
    exit(out)

fn_out_shape = None  # Figure out proper shape.
row_splits_dtype = (
    a.row_splits.dtype
    if isinstance(a, ragged_tensor.RaggedTensor) else b.row_splits.dtype)
output_type = kwargs['output_type']
if output_type is None:
    output_type = a.dtype
spec = ragged_tensor.RaggedTensorSpec(
    shape=fn_out_shape,
    dtype=output_type,
    ragged_rank=output_ragged_rank - 1,
    row_splits_dtype=row_splits_dtype)
result = map_fn.map_fn(
    single_batch_matmul, elems=(a, b), fn_output_signature=spec)

# map_fn loses shape information; restore it, where possible.
# pylint: disable=protected-access
if kwargs.get('transpose_a') or kwargs.get('adjoint_a'):
    result._set_shape(a.shape[:-2] + a.shape[-1:] + [None])
else:
    result._set_shape(a.shape[:-2] + a.shape[-2:-1] + [None])
if kwargs.get('transpose_b') or kwargs.get('adjoint_b'):
    result._set_shape(b.shape[:-2] + [None] + b.shape[-2:-1])
else:
    result._set_shape(b.shape[:-2] + [None] + b.shape[-1:])

exit(result)
