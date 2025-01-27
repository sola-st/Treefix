# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Randomly flip an image horizontally (left to right).

  With a 1 in 2 chance, outputs the contents of `image` flipped along the
  second dimension, which is `width`.  Otherwise output the image as-is.
  When passing a batch of images, each image will be randomly flipped
  independent of other images.

  Example usage:

  >>> image = np.array([[[1], [2]], [[3], [4]]])
  >>> tf.image.random_flip_left_right(image, 5).numpy().tolist()
  [[[2], [1]], [[4], [3]]]

  Randomly flip multiple images.

  >>> images = np.array(
  ... [
  ...     [[[1], [2]], [[3], [4]]],
  ...     [[[5], [6]], [[7], [8]]]
  ... ])
  >>> tf.image.random_flip_left_right(images, 6).numpy().tolist()
  [[[[2], [1]], [[4], [3]]], [[[5], [6]], [[7], [8]]]]

  For producing deterministic results given a `seed` value, use
  `tf.image.stateless_random_flip_left_right`. Unlike using the `seed` param
  with `tf.image.random_*` ops, `tf.image.stateless_random_*` ops guarantee the
  same results given the same seed independent of how many times the function is
  called, and independent of global seed settings (e.g. tf.random.set_seed).

  Args:
    image: 4-D Tensor of shape `[batch, height, width, channels]` or 3-D Tensor
      of shape `[height, width, channels]`.
    seed: A Python integer. Used to create a random seed. See
      `tf.compat.v1.set_random_seed` for behavior.

  Returns:
    A tensor of the same type and shape as `image`.

  Raises:
    ValueError: if the shape of `image` not supported.
  """
random_func = functools.partial(random_ops.random_uniform, seed=seed)
exit(_random_flip(image, 1, random_func, 'random_flip_left_right'))
