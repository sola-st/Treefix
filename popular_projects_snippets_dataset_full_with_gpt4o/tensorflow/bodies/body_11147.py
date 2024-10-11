# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Generate a randomly distorted bounding box for an image deterministically.

  Bounding box annotations are often supplied in addition to ground-truth labels
  in image recognition or object localization tasks. A common technique for
  training such a system is to randomly distort an image while preserving
  its content, i.e. *data augmentation*. This Op, given the same `seed`,
  deterministically outputs a randomly distorted localization of an object, i.e.
  bounding box, given an `image_size`, `bounding_boxes` and a series of
  constraints.

  The output of this Op is a single bounding box that may be used to crop the
  original image. The output is returned as 3 tensors: `begin`, `size` and
  `bboxes`. The first 2 tensors can be fed directly into `tf.slice` to crop the
  image. The latter may be supplied to `tf.image.draw_bounding_boxes` to
  visualize what the bounding box looks like.

  Bounding boxes are supplied and returned as `[y_min, x_min, y_max, x_max]`.
  The bounding box coordinates are floats in `[0.0, 1.0]` relative to the width
  and the height of the underlying image.

  The output of this Op is guaranteed to be the same given the same `seed` and
  is independent of how many times the function is called, and independent of
  global seed settings (e.g. `tf.random.set_seed`).

  Example usage:

  >>> image = np.array([[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]])
  >>> bbox = tf.constant(
  ...   [0.0, 0.0, 1.0, 1.0], dtype=tf.float32, shape=[1, 1, 4])
  >>> seed = (1, 2)
  >>> # Generate a single distorted bounding box.
  >>> bbox_begin, bbox_size, bbox_draw = (
  ...   tf.image.stateless_sample_distorted_bounding_box(
  ...     tf.shape(image), bounding_boxes=bbox, seed=seed))
  >>> # Employ the bounding box to distort the image.
  >>> tf.slice(image, bbox_begin, bbox_size)
  <tf.Tensor: shape=(2, 2, 1), dtype=int64, numpy=
  array([[[1],
          [2]],
         [[4],
          [5]]])>
  >>> # Draw the bounding box in an image summary.
  >>> colors = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
  >>> tf.image.draw_bounding_boxes(
  ...   tf.expand_dims(tf.cast(image, tf.float32),0), bbox_draw, colors)
  <tf.Tensor: shape=(1, 3, 3, 1), dtype=float32, numpy=
  array([[[[1.],
           [1.],
           [3.]],
          [[1.],
           [1.],
           [6.]],
          [[7.],
           [8.],
           [9.]]]], dtype=float32)>

  Note that if no bounding box information is available, setting
  `use_image_if_no_bounding_boxes = true` will assume there is a single implicit
  bounding box covering the whole image. If `use_image_if_no_bounding_boxes` is
  false and no bounding boxes are supplied, an error is raised.

  Args:
    image_size: A `Tensor`. Must be one of the following types: `uint8`, `int8`,
      `int16`, `int32`, `int64`. 1-D, containing `[height, width, channels]`.
    bounding_boxes: A `Tensor` of type `float32`. 3-D with shape `[batch, N, 4]`
      describing the N bounding boxes associated with the image.
    seed: A shape [2] Tensor, the seed to the random number generator. Must have
      dtype `int32` or `int64`. (When using XLA, only `int32` is allowed.)
    min_object_covered: A Tensor of type `float32`. Defaults to `0.1`. The
      cropped area of the image must contain at least this fraction of any
      bounding box supplied. The value of this parameter should be non-negative.
      In the case of 0, the cropped area does not need to overlap any of the
      bounding boxes supplied.
    aspect_ratio_range: An optional list of `floats`. Defaults to `[0.75,
      1.33]`. The cropped area of the image must have an aspect `ratio = width /
      height` within this range.
    area_range: An optional list of `floats`. Defaults to `[0.05, 1]`. The
      cropped area of the image must contain a fraction of the supplied image
      within this range.
    max_attempts: An optional `int`. Defaults to `100`. Number of attempts at
      generating a cropped region of the image of the specified constraints.
      After `max_attempts` failures, return the entire image.
    use_image_if_no_bounding_boxes: An optional `bool`. Defaults to `False`.
      Controls behavior if no bounding boxes supplied. If true, assume an
      implicit bounding box covering the whole input. If false, raise an error.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (begin, size, bboxes).

    begin: A `Tensor`. Has the same type as `image_size`. 1-D, containing
    `[offset_height, offset_width, 0]`. Provide as input to
      `tf.slice`.
    size: A `Tensor`. Has the same type as `image_size`. 1-D, containing
    `[target_height, target_width, -1]`. Provide as input to
      `tf.slice`.
    bboxes: A `Tensor` of type `float32`. 3-D with shape `[1, 1, 4]` containing
    the distorted bounding box.
    Provide as input to `tf.image.draw_bounding_boxes`.
  """
with ops.name_scope(name, 'stateless_sample_distorted_bounding_box'):
    exit(gen_image_ops.stateless_sample_distorted_bounding_box(
        image_size=image_size,
        bounding_boxes=bounding_boxes,
        seed=seed,
        min_object_covered=min_object_covered,
        aspect_ratio_range=aspect_ratio_range,
        area_range=area_range,
        max_attempts=max_attempts,
        use_image_if_no_bounding_boxes=use_image_if_no_bounding_boxes,
        name=name))
