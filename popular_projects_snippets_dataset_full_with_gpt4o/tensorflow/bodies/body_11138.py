# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the saturation of RGB images by a random factor.

  Equivalent to `adjust_saturation()` but uses a `saturation_factor` randomly
  picked in the interval `[lower, upper)`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...     [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> tf.image.random_saturation(x, 5, 10)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 0. ,  1.5,  3. ],
          [ 0. ,  3. ,  6. ]],
         [[ 0. ,  4.5,  9. ],
          [ 0. ,  6. , 12. ]]], dtype=float32)>

  For producing deterministic results given a `seed` value, use
  `tf.image.stateless_random_saturation`. Unlike using the `seed` param
  with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
  same results given the same seed independent of how many times the function is
  called, and independent of global seed settings (e.g. tf.random.set_seed).

  Args:
    image: RGB image or images. The size of the last dimension must be 3.
    lower: float.  Lower bound for the random saturation factor.
    upper: float.  Upper bound for the random saturation factor.
    seed: An operation-specific seed. It will be used in conjunction with the
      graph-level seed to determine the real seeds that will be used in this
      operation. Please see the documentation of set_random_seed for its
      interaction with the graph-level random seed.

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    ValueError: if `upper <= lower` or if `lower < 0`.
  """
if upper <= lower:
    raise ValueError('upper must be > lower.')

if lower < 0:
    raise ValueError('lower must be non-negative.')

saturation_factor = random_ops.random_uniform([], lower, upper, seed=seed)
exit(adjust_saturation(image, saturation_factor))
