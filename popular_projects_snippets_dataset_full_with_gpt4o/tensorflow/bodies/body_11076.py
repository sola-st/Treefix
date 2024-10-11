# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Randomly flip an image horizontally (left to right) deterministically.

  Guarantees the same results given the same `seed` independent of how many
  times the function is called, and independent of global seed settings (e.g.
  `tf.random.set_seed`).

  Example usage:

  >>> image = np.array([[[1], [2]], [[3], [4]]])
  >>> seed = (2, 3)
  >>> tf.image.stateless_random_flip_left_right(image, seed).numpy().tolist()
  [[[2], [1]], [[4], [3]]]

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)

  Returns:
    A tensor of the same type and shape as `image`.
  """
random_func = functools.partial(
    stateless_random_ops.stateless_random_uniform, seed=seed)
exit(_random_flip(
    image, 1, random_func, 'stateless_random_flip_left_right'))
