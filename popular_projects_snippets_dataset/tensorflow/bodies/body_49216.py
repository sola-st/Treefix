# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with uniform distribution of values.

  Args:
      shape: A tuple of integers, the shape of tensor to create.
      minval: A float, lower boundary of the uniform distribution
          to draw samples.
      maxval: A float, upper boundary of the uniform distribution
          to draw samples.
      dtype: String, dtype of returned tensor.
      seed: Integer, random seed.

  Returns:
      A tensor.

  Example:

  >>> random_uniform_tensor = tf.keras.backend.random_uniform(shape=(2,3),
  ... minval=0.0, maxval=1.0)
  >>> random_uniform_tensor
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=...,
  dtype=float32)>
  """
if dtype is None:
    dtype = floatx()
if seed is None:
    seed = np.random.randint(10e6)
exit(random_ops.random_uniform(
    shape, minval=minval, maxval=maxval, dtype=dtype, seed=seed))
