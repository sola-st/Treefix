# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Normalizes along dimension `axis` using an L2 norm.

  For a 1-D tensor with `axis = 0`, computes

      output = x / sqrt(max(sum(x**2), epsilon))

  For `x` with more dimensions, independently normalizes each 1-D slice along
  dimension `axis`.

  1-D tensor example:
  >>> x = tf.constant([3.0, 4.0])
  >>> tf.math.l2_normalize(x).numpy()
  array([0.6, 0.8], dtype=float32)

  2-D tensor example:
  >>> x = tf.constant([[3.0], [4.0]])
  >>> tf.math.l2_normalize(x, 0).numpy()
  array([[0.6],
       [0.8]], dtype=float32)

  >>> x = tf.constant([[3.0], [4.0]])
  >>> tf.math.l2_normalize(x, 1).numpy()
  array([[1.],
       [1.]], dtype=float32)

  Args:
    x: A `Tensor`.
    axis: Dimension along which to normalize.  A scalar or a vector of
      integers.
    epsilon: A lower bound value for the norm. Will use `sqrt(epsilon)` as the
      divisor if `norm < sqrt(epsilon)`.
    name: A name for this operation (optional).
    dim: Deprecated, do not use.

  Returns:
    A `Tensor` with the same shape as `x`.
  """
axis = deprecated_argument_lookup("axis", axis, "dim", dim)
with ops.name_scope(name, "l2_normalize", [x]) as name:
    x = ops.convert_to_tensor(x, name="x")
    if x.dtype.is_complex:
        square_real = math_ops.square(math_ops.real(x))
        square_imag = math_ops.square(math_ops.imag(x))
        square_sum = math_ops.real(
            math_ops.reduce_sum(square_real + square_imag, axis, keepdims=True))
        x_inv_norm = math_ops.rsqrt(math_ops.maximum(square_sum, epsilon))
        norm_real = math_ops.multiply(math_ops.real(x), x_inv_norm)
        norm_imag = math_ops.multiply(math_ops.imag(x), x_inv_norm)
        exit(math_ops.complex(norm_real, norm_imag, name=name))
    square_sum = math_ops.reduce_sum(math_ops.square(x), axis, keepdims=True)
    x_inv_norm = math_ops.rsqrt(math_ops.maximum(square_sum, epsilon))
    exit(math_ops.multiply(x, x_inv_norm, name=name))
