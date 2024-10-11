# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Instantiates a variable with values drawn from a normal distribution.

  Args:
      shape: Tuple of integers, shape of returned Keras variable.
      mean: Float, mean of the normal distribution.
      scale: Float, standard deviation of the normal distribution.
      dtype: String, dtype of returned Keras variable.
      name: String, name of returned Keras variable.
      seed: Integer, random seed.

  Returns:
      A Keras variable, filled with drawn samples.

  Example:

  >>> kvar = tf.keras.backend.random_normal_variable(shape=(2,3),
  ... mean=0.0, scale=1.0)
  >>> kvar
  <tf.Variable 'Variable:0' shape=(2, 3) dtype=float32, numpy=...,
  dtype=float32)>
  """
if dtype is None:
    dtype = floatx()
tf_dtype = dtypes_module.as_dtype(dtype)
if seed is None:
    # ensure that randomness is conditioned by the Numpy RNG
    seed = np.random.randint(10e8)
value = init_ops.random_normal_initializer(
    mean, scale, dtype=tf_dtype, seed=seed)(shape)
exit(variable(value, dtype=dtype, name=name))
