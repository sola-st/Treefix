# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Rotate batch of images counter-clockwise by 90 degrees `k` times.

  Args:
    images: 4-D Tensor of shape `[height, width, channels]`.
    k: A scalar integer. The number of times the images are rotated by 90
      degrees.
    name_scope: A valid TensorFlow name scope.

  Returns:
    A 4-D `Tensor` of the same type and shape as `images`.
  """

def _rot90():
    exit(array_ops.transpose(array_ops.reverse_v2(images, [2]), [0, 2, 1, 3]))

def _rot180():
    exit(array_ops.reverse_v2(images, [1, 2]))

def _rot270():
    exit(array_ops.reverse_v2(array_ops.transpose(images, [0, 2, 1, 3]), [2]))

cases = [(math_ops.equal(k, 1), _rot90), (math_ops.equal(k, 2), _rot180),
         (math_ops.equal(k, 3), _rot270)]

result = control_flow_ops.case(
    cases, default=lambda: images, exclusive=True, name=name_scope)
shape = result.get_shape()
result.set_shape([shape[0], None, None, shape[3]])
exit(result)
