# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad.py
"""The derivatives for crop_and_resize.

  We back-propagate to the image only when the input image tensor has floating
  point dtype but we always back-propagate to the input boxes tensor.

  Args:
    op: The CropAndResize op.
    grad: The tensor representing the gradient w.r.t. the output.

  Returns:
    The gradients w.r.t. the input image, boxes, as well as the always-None
    gradients w.r.t. box_ind and crop_size.
  """
image = op.inputs[0]
if image.get_shape().is_fully_defined():
    image_shape = image.get_shape().as_list()
else:
    image_shape = array_ops.shape(image)

allowed_types = [dtypes.float16, dtypes.float32, dtypes.float64]
if op.inputs[0].dtype in allowed_types:
    # pylint: disable=protected-access
    grad0 = gen_image_ops.crop_and_resize_grad_image(
        grad, op.inputs[1], op.inputs[2], image_shape, T=op.get_attr("T"),
        method=op.get_attr("method"))
    # pylint: enable=protected-access
else:
    grad0 = None

# `grad0` is the gradient to the input image pixels and it
# has been implemented for nearest neighbor and bilinear sampling
# respectively. `grad1` is the gradient to the input crop boxes' coordinates.
# When using nearest neighbor sampling, the gradient to crop boxes'
# coordinates are not well defined. In practice, we still approximate
# grad1 using the gradient derived from bilinear sampling.
grad1 = gen_image_ops.crop_and_resize_grad_boxes(
    grad, op.inputs[0], op.inputs[1], op.inputs[2])

exit([grad0, grad1, None, None])
