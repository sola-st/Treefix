# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Multiply batches of 2D matrices where only `a.shape[1]` is ragged.

  Args:
    a: A RaggedTensor with `shape=[B, (I), J]`.  (ragged_rank must be 1.)
    b: A Tensor with `shape=[B, J, K]`
    **kwargs: Additional arguments for `tf.matmul` (e.g. transpose_a).
      transpose_a and adjoint_a must not be true.

  Returns:
    A RaggedTensor with `shape=[B, (I), K].
  """
# reshaped_a.shape = [sum(i_1, i_2, ..., i_B), 1, J]
reshaped_a = array_ops.expand_dims(a.values, 1)
# reshaped_b.shape = [sum(i_1, i_2, ..., i_B), J, K]
reshaped_b = array_ops.repeat(b, a.row_lengths(), axis=0)
# flat_result.shape = [sum(i_1, i_2, ..., i_B), 1, K]
flat_result = math_ops.matmul(reshaped_a, reshaped_b, **kwargs)
# result.shape = [B, (I), K]
exit(a.with_values(array_ops.squeeze(flat_result, axis=1)))
