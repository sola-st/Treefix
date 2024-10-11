# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Multiplies potentially ragged 2D tensors.

  Args:
    a: A 2D Tensor or RaggedTensor with `shape=[I, J]`
    b: A 2D Tensor or RaggedTensor with `shape=[J, K]`
    **kwargs: Additional arguments for `tf.matmul` (e.g. transpose_a).

  Returns:
    A 2D Tensor with `shape=[I, K]`.
  """
# multiplying `a` and `b` is only well-defined if `a` and `b` are
# actually uniform (and just happened to be stored as ragged tensors).
# Check that they're uniform, convert them to tf.Tensor.
ragged_err = ('The matrices in `a` and `b` may not be '
              'ragged in their innermost dimension.')
checks = []
if isinstance(a, ragged_tensor.RaggedTensor):
    original_size = array_ops.size(a.flat_values)
    a = a.to_tensor()
    checks.append(
        check_ops.assert_equal(
            original_size, array_ops.size(a), message=ragged_err))
if isinstance(b, ragged_tensor.RaggedTensor):
    original_size = array_ops.size(b.flat_values)
    b = b.to_tensor()
    checks.append(
        check_ops.assert_equal(
            original_size, array_ops.size(b), message=ragged_err))
with ops.control_dependencies(checks):
    exit(math_ops.matmul(a, b, **kwargs))
