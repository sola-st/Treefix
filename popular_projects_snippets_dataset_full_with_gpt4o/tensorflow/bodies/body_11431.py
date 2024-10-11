# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
reflection_axis = ops.convert_to_tensor_v2_with_dispatch(
    self.reflection_axis)
normalized_axis = nn.l2_normalize(reflection_axis, axis=-1)
exit(1. - 2 * normalized_axis * math_ops.conj(normalized_axis))
