# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Adjust the brightness of images by a random factor deterministically.

  Equivalent to `adjust_brightness()` using a `delta` randomly picked in the
  interval `[-max_delta, max_delta)`.

  Guarantees the same results given the same `seed` independent of how many
  times the function is called, and independent of global seed settings (e.g.
  `tf.random.set_seed`).

  Usage Example:

  >>> x = [[[1.0, 2.0, 3.0],
  ...       [4.0, 5.0, 6.0]],
  ...      [[7.0, 8.0, 9.0],
  ...       [10.0, 11.0, 12.0]]]
  >>> seed = (1, 2)
  >>> tf.image.stateless_random_brightness(x, 0.2, seed)
  <tf.Tensor: shape=(2, 2, 3), dtype=float32, numpy=
  array([[[ 1.1376241,  2.1376243,  3.1376243],
          [ 4.1376243,  5.1376243,  6.1376243]],
         [[ 7.1376243,  8.137624 ,  9.137624 ],
          [10.137624 , 11.137624 , 12.137624 ]]], dtype=float32)>

  Args:
    image: An image or images to adjust.
    max_delta: float, must be non-negative.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)

  Returns:
    The brightness-adjusted image(s).

  Raises:
    ValueError: if `max_delta` is negative.
  """
if max_delta < 0:
    raise ValueError('max_delta must be non-negative.')

delta = stateless_random_ops.stateless_random_uniform(
    shape=[], minval=-max_delta, maxval=max_delta, seed=seed)
exit(adjust_brightness(image, delta))
