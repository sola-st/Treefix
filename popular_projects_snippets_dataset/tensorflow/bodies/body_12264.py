# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Creates a tensor with all elements set to zero.

  See also `tf.zeros`.

  Given a single tensor (`tensor`), this operation returns a tensor of the
  same type and shape as `tensor` with all elements set to zero. Optionally,
  you can use `dtype` to specify a new type for the returned tensor.

  Examples:

    >>> tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
    >>> tf.zeros_like(tensor)
    <tf.Tensor: shape=(2, 3), dtype=int32, numpy=
    array([[0, 0, 0],
           [0, 0, 0]], dtype=int32)>

    >>> tf.zeros_like(tensor, dtype=tf.float32)
    <tf.Tensor: shape=(2, 3), dtype=float32, numpy=
    array([[0., 0., 0.],
           [0., 0., 0.]], dtype=float32)>

  Args:
    tensor: A `Tensor`.
    dtype: A type for the returned `Tensor`. Must be `float16`, `float32`,
      `float64`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `int64`,
      `complex64`, `complex128`, `bool` or `string`. (optional)
    name: A name for the operation (optional).
    optimize: if `True`, attempt to statically determine the shape of `tensor`
      and encode it as a constant. (optional, defaults to `True`)

  Returns:
    A `Tensor` with all elements set to zero.
  """
exit(zeros_like_impl(tensor, dtype, name, optimize))
