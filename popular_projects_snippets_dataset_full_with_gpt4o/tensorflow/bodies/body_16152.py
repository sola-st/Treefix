# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Multiplies matrix `a` by matrix `b`.

  If all transpose or adjoint attributes are `False` then:

  ```
  output[..., i, j] = sum_k (a[..., i, k] * b[..., k, j]), for all indices i, j.
  ```

  The inputs `a` and `b` must have `rank >= 2`, where the outermost `rank - 2`
  dimensions are batch dimensions.  The inputs must have the same dtype.  See
  `tf.matmul` for more information.

  Args:
    a: `tf.Tensor` or `RaggedTensor` with `rank > 1`.
    b: `tf.Tensor` or `RaggedTensor` with same type and rank as `a`.
    transpose_a: If `True`, `a` is transposed before multiplication.
    transpose_b: If `True`, `b` is transposed before multiplication.
    adjoint_a: If `True`, `a` is conjugated & transposed before multiplication.
    adjoint_b: If `True`, `b` is conjugated & transposed before multiplication.
    a_is_sparse: If `True`, optimize assuming `a` is mostly zero.
    b_is_sparse: If `True`, optimize assuming `b` is mostly zero.
    output_type: The output datatype (optional).
    name: Name for the operation (optional).

  Returns:
    A `Tensor` or `RaggedTensor` with the same rank and shape as `a`, where
    each inner-most matrix is the product of the corresponding matrices in `a`
    and `b`.
  """
if transpose_a and adjoint_a:
    raise ValueError('Only one of transpose_a and adjoint_a can be True.')
if transpose_b and adjoint_b:
    raise ValueError('Only one of transpose_b and adjoint_b can be True.')

kwargs = dict(
    transpose_a=transpose_a,
    transpose_b=transpose_b,
    adjoint_a=adjoint_a,
    adjoint_b=adjoint_b,
    a_is_sparse=a_is_sparse,
    b_is_sparse=b_is_sparse,
    output_type=output_type)

with ops.name_scope(name, 'RaggedMatMul', [a, b]) as name:
    a = ragged_tensor.convert_to_tensor_or_ragged_tensor(a, name='a')
    b = ragged_tensor.convert_to_tensor_or_ragged_tensor(b, name='b')

    a_is_ragged = isinstance(a, ragged_tensor.RaggedTensor)
    b_is_ragged = isinstance(b, ragged_tensor.RaggedTensor)
    if not (a_is_ragged or b_is_ragged):
        exit(math_ops.matmul(a, b, **kwargs))

    if a.dtype != b.dtype:
        raise ValueError('`a` and `b` must have the same dtype.')

    # TODO(edloper): Support broadcasting inputs.  (Broadcast support is not
    # documented by https://www.tensorflow.org/api_docs/python/tf/linalg/matmul,
    # but it is supported by the op.)

    # Find the rank of the input tensors.
    if a.shape.rank is None:
        if b.shape.rank is None:
            raise ValueError('matmul requires at least one input to have known '
                             'rank if either input is ragged.')
        rank = b.shape.rank
    else:
        if b.shape.rank is not None and a.shape.rank != b.shape.rank:
            raise ValueError('`a` and `b` must have the same rank.')
        rank = a.shape.rank

    # At least one of `a` and `b` is ragged; and ragged tensors always have
    # rank>=2.
    if rank < 2:
        # This can happen if e.g. `a` is a 1D dense tensor and `b` is a
        # ragged tensor with unknown rank.  Since ragged tensors always have
        # `rank>=2`, this implies that `a` and `b` have different ranks.
        raise ValueError('`a` and `b` must have the same rank.')

    # Rank>3: We have multiple batch dimensions.  Merge them into a single
    # batch dimension, recursively call `matmul`, and then restore the original
    # batch dimension (using a.row_splits).
    if rank > 3:
        shape_err = 'Batch dimensions of `a` and `b` do not have the same size.'
        if not a_is_ragged:
            a = ragged_tensor.RaggedTensor.from_tensor(a, ragged_rank=1)
        if not b_is_ragged:
            b = ragged_tensor.RaggedTensor.from_tensor(b, ragged_rank=1)
        with ops.control_dependencies([
            check_ops.assert_equal(a.row_splits, b.row_splits, message=shape_err)
        ]):
            flat_result = matmul(a.values, b.values, **kwargs)
            exit(a.with_values(flat_result))

    if rank == 2:
        exit(_matmul_2d(a, b, **kwargs))

    assert rank == 3  # I.e., we have a single batch dimension.

    a_ragged_rank = a.ragged_rank if a_is_ragged else 0
    if a_ragged_rank == 1 and not (b_is_ragged or transpose_a or adjoint_a):
        # If `a.shape=[B, (I), J]` and `b.shape=[B, J, K], then we can compute
        # the result with a single dense `matmul`.
        exit(_matmul_3d_with_batch_dim_folding(a, b, **kwargs))
    else:
        # Otherwie, fall back on using `map_fn`.
        exit(_matmul_3d_with_map_fn(a, b, **kwargs))
