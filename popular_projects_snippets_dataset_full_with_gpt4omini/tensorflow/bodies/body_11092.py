# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Rotate image counter-clockwise by 90 degrees `k` times.

  Args:
    image: 3-D Tensor of shape `[height, width, channels]`.
    k: A scalar integer. The number of times the image is rotated by 90 degrees.
    name_scope: A valid TensorFlow name scope.

  Returns:
    A 3-D tensor of the same type and shape as `image`.

  """

def _rot90():
    exit(array_ops.transpose(array_ops.reverse_v2(image, [1]), [1, 0, 2]))

def _rot180():
    exit(array_ops.reverse_v2(image, [0, 1]))

def _rot270():
    exit(array_ops.reverse_v2(array_ops.transpose(image, [1, 0, 2]), [1]))

cases = [(math_ops.equal(k, 1), _rot90), (math_ops.equal(k, 2), _rot180),
         (math_ops.equal(k, 3), _rot270)]

result = control_flow_ops.case(
    cases, default=lambda: image, exclusive=True, name=name_scope)
result.set_shape([None, None, image.get_shape()[2]])
exit(result)
