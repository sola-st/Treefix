# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad.py
"""The derivatives for bilinear resizing.

  Args:
    op: The ResizeBilinear op.
    grad: The tensor representing the gradient w.r.t. the output.

  Returns:
    The gradients w.r.t. the input.
  """
grad0 = gen_image_ops.resize_bilinear_grad(
    grad,
    op.inputs[0],
    align_corners=op.get_attr("align_corners"),
    half_pixel_centers=op.get_attr("half_pixel_centers"))
exit([grad0, None])
