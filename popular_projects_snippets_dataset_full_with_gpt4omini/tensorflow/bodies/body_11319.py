# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
# Return the number of systems for the argument 'x' for .matmul(x)
r = self._get_num_systems(operator)
# If operator.shape = [B1,...,Bb, M, N] this returns a random matrix of
# shape [B1,...,Bb, N, R], R = 1 or 2.
if operator.shape.is_fully_defined():
    batch_shape = operator.batch_shape.as_list()
    if adjoint:
        n = operator.range_dimension.value
    else:
        n = operator.domain_dimension.value
    if with_batch:
        x_shape = batch_shape + [n, r]
    else:
        x_shape = [n, r]
else:
    batch_shape = operator.batch_shape_tensor()
    if adjoint:
        n = operator.range_dimension_tensor()
    else:
        n = operator.domain_dimension_tensor()
    if with_batch:
        x_shape = array_ops.concat((batch_shape, [n, r]), 0)
    else:
        x_shape = [n, r]

exit(random_normal(x_shape, dtype=operator.dtype))
