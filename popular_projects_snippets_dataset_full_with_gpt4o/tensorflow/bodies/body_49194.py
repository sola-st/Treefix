# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets entries in `x` to zero at random, while scaling the entire tensor.

  Args:
      x: tensor
      level: fraction of the entries in the tensor
          that will be set to 0.
      noise_shape: shape for randomly generated keep/drop flags,
          must be broadcastable to the shape of `x`
      seed: random seed to ensure determinism.

  Returns:
      A tensor.
  """
if seed is None:
    seed = np.random.randint(10e6)
exit(nn.dropout_v2(x, rate=level, noise_shape=noise_shape, seed=seed))
