# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns a tensor with truncated random normal distribution of values.

  The generated values follow a normal distribution
  with specified mean and standard deviation,
  except that values whose magnitude is more than
  two standard deviations from the mean are dropped and re-picked.

  Args:
      shape: A tuple of integers, the shape of tensor to create.
      mean: Mean of the values.
      stddev: Standard deviation of the values.
      dtype: String, dtype of returned tensor.
      seed: Integer, random seed.

  Returns:
      A tensor.
  """
if dtype is None:
    dtype = floatx()
if seed is None:
    seed = np.random.randint(10e6)
exit(random_ops.truncated_normal(
    shape, mean, stddev, dtype=dtype, seed=seed))
