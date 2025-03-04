# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with normal distribution of values.

  It is an alias to `tf.random.normal`.

  Args:
      shape: A tuple of integers, the shape of tensor to create.
      mean: A float, the mean value of the normal distribution to draw samples.
        Default to 0.0.
      stddev: A float, the standard deviation of the normal distribution
        to draw samples. Default to 1.0.
      dtype: `tf.dtypes.DType`, dtype of returned tensor. Default to use Keras
        backend dtype which is float32.
      seed: Integer, random seed. Will use a random numpy integer when not
        specified.

  Returns:
      A tensor with normal distribution of values.

  Example:

  >>> random_normal_tensor = tf.keras.backend.random_normal(shape=(2,3),
  ... mean=0.0, stddev=1.0)
  >>> random_normal_tensor
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=...,
  dtype=float32)>
  """
if dtype is None:
    dtype = floatx()
if seed is None:
    seed = np.random.randint(10e6)
exit(random_ops.random_normal(
    shape, mean=mean, stddev=stddev, dtype=dtype, seed=seed))
