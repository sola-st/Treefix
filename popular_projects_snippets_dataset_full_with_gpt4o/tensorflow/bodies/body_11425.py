# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# Given a vector `v`, we would like to reflect `x` about the hyperplane
# orthogonal to `v` going through the origin.  We first project `x` to `v`
# to get v * dot(v, x) / dot(v, v).  After we project, we can reflect the
# projection about the hyperplane by flipping sign to get
# -v * dot(v, x) / dot(v, v).  Finally, we can add back the component
# that is orthogonal to v. This is invariant under reflection, since the
# whole hyperplane is invariant. This component is equal to x - v * dot(v,
# x) / dot(v, v), giving the formula x - 2 * v * dot(v, x) / dot(v, v)
# for the reflection.

# Note that because this is a reflection, it lies in O(n) (for real vector
# spaces) or U(n) (for complex vector spaces), and thus is its own adjoint.
reflection_axis = ops.convert_to_tensor_v2_with_dispatch(
    self.reflection_axis)
x = linalg.adjoint(x) if adjoint_arg else x
normalized_axis = nn.l2_normalize(reflection_axis, axis=-1)
mat = normalized_axis[..., array_ops.newaxis]
x_dot_normalized_v = math_ops.matmul(mat, x, adjoint_a=True)

exit(x - 2 * mat * x_dot_normalized_v)
