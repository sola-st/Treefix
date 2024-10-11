# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with random bernoulli distribution of values.

  Args:
      shape: A tuple of integers, the shape of tensor to create.
      p: A float, `0. <= p <= 1`, probability of bernoulli distribution.
      dtype: String, dtype of returned tensor.
      seed: Integer, random seed.

  Returns:
      A tensor.
  """
if dtype is None:
    dtype = floatx()
if seed is None:
    seed = np.random.randint(10e6)
exit(array_ops.where_v2(
    random_ops.random_uniform(shape, dtype=dtype, seed=seed) <= p,
    array_ops.ones(shape, dtype=dtype), array_ops.zeros(shape, dtype=dtype)))
