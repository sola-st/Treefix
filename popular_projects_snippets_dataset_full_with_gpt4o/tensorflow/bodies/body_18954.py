# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Multiplies a scalar times a `Tensor` or `IndexedSlices` object.

  This is a special case of `tf.math.multiply`, where the first value must be a
  `scalar`. Unlike the general form of `tf.math.multiply`, this is operation is
  guaranteed to be efficient for `tf.IndexedSlices`.

  >>> x = tf.reshape(tf.range(30, dtype=tf.float32), [10, 3])
  >>> with tf.GradientTape() as g:
  ...   g.watch(x)
  ...   y = tf.gather(x, [1, 2])  # IndexedSlices
  ...   z = tf.math.scalar_mul(10.0, y)

  Args:
    scalar: A 0-D scalar `Tensor`. Must have known shape.
    x: A `Tensor` or `IndexedSlices` to be scaled.
    name: A name for the operation (optional).

  Returns:
    `scalar * x` of the same type (`Tensor` or `IndexedSlices`) as `x`.

  Raises:
    ValueError: if scalar is not a 0-D `scalar`.
  """
base_dtype = dtypes.as_dtype(x.dtype).base_dtype
scalar = ops.convert_to_tensor(
    scalar, dtype=base_dtype, name="scalar")
shape = scalar.get_shape()
if shape.ndims == 0:
    if isinstance(x, indexed_slices.IndexedSlices):
        exit(indexed_slices.IndexedSlices(
            gen_math_ops.mul(scalar, x.values, name), x.indices, x.dense_shape))
    else:
        exit(gen_math_ops.mul(scalar, x, name))
else:
    raise ValueError(
        f"The input scalar must be a 0-D value. Received shape {shape}.")
