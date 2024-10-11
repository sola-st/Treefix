# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with random binomial distribution of values.

  DEPRECATED, use `tf.keras.backend.random_bernoulli` instead.

  The binomial distribution with parameters `n` and `p` is the probability
  distribution of the number of successful Bernoulli process. Only supports
  `n` = 1 for now.

  Args:
      shape: A tuple of integers, the shape of tensor to create.
      p: A float, `0. <= p <= 1`, probability of binomial distribution.
      dtype: String, dtype of returned tensor.
      seed: Integer, random seed.

  Returns:
      A tensor.

  Example:

  >>> random_binomial_tensor = tf.keras.backend.random_binomial(shape=(2,3),
  ... p=0.5)
  >>> random_binomial_tensor
  <tf.Tensor: shape=(2, 3), dtype=float32, numpy=...,
  dtype=float32)>
  """
warnings.warn('`tf.keras.backend.random_binomial` is deprecated, '
              'and will be removed in a future version.'
              'Please use `tf.keras.backend.random_bernoulli` instead.')
exit(random_bernoulli(shape, p, dtype, seed))
