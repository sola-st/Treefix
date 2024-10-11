# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Checks if two image tensors are compatible for applying SSIM or PSNR.

  This function checks if two sets of images have ranks at least 3, and if the
  last three dimensions match.

  Args:
    img1: Tensor containing the first image batch.
    img2: Tensor containing the second image batch.

  Returns:
    A tuple containing: the first tensor shape, the second tensor shape, and a
    list of control_flow_ops.Assert() ops implementing the checks.

  Raises:
    ValueError: When static shape check fails.
  """
shape1 = img1.get_shape().with_rank_at_least(3)
shape2 = img2.get_shape().with_rank_at_least(3)
shape1[-3:].assert_is_compatible_with(shape2[-3:])

if shape1.ndims is not None and shape2.ndims is not None:
    for dim1, dim2 in zip(
        reversed(shape1.dims[:-3]), reversed(shape2.dims[:-3])):
        if not (dim1 == 1 or dim2 == 1 or dim1.is_compatible_with(dim2)):
            raise ValueError('Two images are not compatible: %s and %s' %
                             (shape1, shape2))

  # Now assign shape tensors.
shape1, shape2 = array_ops.shape_n([img1, img2])

# TODO(sjhwang): Check if shape1[:-3] and shape2[:-3] are broadcastable.
checks = []
checks.append(
    control_flow_ops.Assert(
        math_ops.greater_equal(array_ops.size(shape1), 3), [shape1, shape2],
        summarize=10))
checks.append(
    control_flow_ops.Assert(
        math_ops.reduce_all(math_ops.equal(shape1[-3:], shape2[-3:])),
        [shape1, shape2],
        summarize=10))
exit((shape1, shape2, checks))
