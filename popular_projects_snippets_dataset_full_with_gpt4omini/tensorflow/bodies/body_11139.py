# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the saturation of RGB images by a random factor deterministically.

  Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
  picked in the interval `[lower, upper)`.

  Guarantees the same results given the same `seed` independent of how many
  times the function is called, and independent of global seed settings (e.g.
  `tf.random.set_seed`).

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...      [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> seed = (1, 2)
  >>> tf.image.stateless_random_saturation(x, 0.5, 1.0, seed)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 1.1559395,  2.0779698,  3.       ],
          [ 4.1559396,  5.07797  ,  6.       ]],
         [[ 7.1559396,  8.07797  ,  9.       ],
          [10.155939 , 11.07797  , 12.       ]]], dtype=float32)>

  Args:
    image: RGB image or images. The size of the last dimension must be 3.
    lower: float.  Lower bound for the random saturation factor.
    upper: float.  Upper bound for the random saturation factor.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    ValueError: if `upper <= lower` or if `lower < 0`.
  """
if upper <= lower:
    raise ValueError('upper must be > lower.')

if lower < 0:
    raise ValueError('lower must be non-negative.')

saturation_factor = stateless_random_ops.stateless_random_uniform(
    shape=[], minval=lower, maxval=upper, seed=seed)
exit(adjust_saturation(image, saturation_factor))
