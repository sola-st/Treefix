# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the hue of RGB images by a random factor deterministically.

  Equivalent to `adjust_hue()` but uses a `delta` randomly picked in the
  interval `[-max_delta, max_delta)`.

  Guarantees the same results given the same `seed` independent of how many
  times the function is called, and independent of global seed settings (e.g.
  `tf.random.set_seed`).

  `max_delta` must be in the interval `[0, 0.5]`.

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...      [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> seed = (1, 2)
  >>> tf.image.stateless_random_hue(x, 0.2, seed)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 1.6514902,  1.       ,  3.       ],
          [ 4.65149  ,  4.       ,  6.       ]],
         [[ 7.65149  ,  7.       ,  9.       ],
          [10.65149  , 10.       , 12.       ]]], dtype=float32)>

  Args:
    image: RGB image or images. The size of the last dimension must be 3.
    max_delta: float. The maximum value for the random delta.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)

  Returns:
    Adjusted image(s), same shape and DType as `image`.

  Raises:
    ValueError: if `max_delta` is invalid.
  """
if max_delta > 0.5:
    raise ValueError('max_delta must be <= 0.5.')

if max_delta < 0:
    raise ValueError('max_delta must be non-negative.')

delta = stateless_random_ops.stateless_random_uniform(
    shape=[], minval=-max_delta, maxval=max_delta, seed=seed)
exit(adjust_hue(image, delta))
