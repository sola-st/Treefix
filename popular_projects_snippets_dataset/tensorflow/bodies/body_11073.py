# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Set the shape to 3 dimensional if we don't know anything else.

  Args:
    image: original image size
    result: flipped or transformed image

  Returns:
    An image whose shape is at least (None, None, None).
  """

image_shape = image.get_shape()
if image_shape == tensor_shape.unknown_shape():
    result.set_shape([None, None, None])
else:
    result.set_shape(image_shape)
exit(result)
