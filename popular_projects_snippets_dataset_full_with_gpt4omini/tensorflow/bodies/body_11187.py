# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Draw bounding boxes on a batch of images.

  Outputs a copy of `images` but draws on top of the pixels zero or more
  bounding boxes specified by the locations in `boxes`. The coordinates of the
  each bounding box in `boxes` are encoded as `[y_min, x_min, y_max, x_max]`.
  The bounding box coordinates are floats in `[0.0, 1.0]` relative to the width
  and the height of the underlying image.

  For example, if an image is 100 x 200 pixels (height x width) and the bounding
  box is `[0.1, 0.2, 0.5, 0.9]`, the upper-left and bottom-right coordinates of
  the bounding box will be `(40, 10)` to `(180, 50)` (in (x,y) coordinates).

  Parts of the bounding box may fall outside the image.

  Args:
    images: A `Tensor`. Must be one of the following types: `float32`, `half`.
      4-D with shape `[batch, height, width, depth]`. A batch of images.
    boxes: A `Tensor` of type `float32`. 3-D with shape `[batch,
      num_bounding_boxes, 4]` containing bounding boxes.
    name: A name for the operation (optional).
    colors: A `Tensor` of type `float32`. 2-D. A list of RGBA colors to cycle
      through for the boxes.

  Returns:
    A `Tensor`. Has the same type as `images`.

  Usage Example:

  >>> # create an empty image
  >>> img = tf.zeros([1, 3, 3, 3])
  >>> # draw a box around the image
  >>> box = np.array([0, 0, 1, 1])
  >>> boxes = box.reshape([1, 1, 4])
  >>> # alternate between red and blue
  >>> colors = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
  >>> tf.image.draw_bounding_boxes(img, boxes, colors)
  <tf.Tensor: shape=(1, 3, 3, 3), dtype=float32, numpy=
  array([[[[1., 0., 0.],
          [1., 0., 0.],
          [1., 0., 0.]],
          [[1., 0., 0.],
          [0., 0., 0.],
          [1., 0., 0.]],
          [[1., 0., 0.],
          [1., 0., 0.],
          [1., 0., 0.]]]], dtype=float32)>
  """
exit(draw_bounding_boxes_v2(images, boxes, colors, name))
