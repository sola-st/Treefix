# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random.py
"""Sets the seed for the random number generator.

  Uses `tf.set_random_seed`.

  Args:
    s: an integer.
  """
try:
    s = int(s)
except TypeError:
    # TODO(wangpeng): support this?
    raise ValueError(
        f'Argument `s` got an invalid value {s}. Only integers are supported.')
random_seed.set_seed(s)
