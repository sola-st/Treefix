# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/xla_control_flow_ops_test.py
x = array_ops.gather(x_series, 0)  # invariant.
y = array_ops.gather(y_series, 0)  # invariant.
x_i = array_ops.gather(x_series, i)
y_i = array_ops.gather(y_series, i)
z1 = xla_ops.einsum(x_i, y, "ab,bc->ac")
z2 = xla_ops.einsum(x, y_i, "ab,bc->ac")
z3 = xla_ops.einsum(x, y, "ab,bc->ac")
z4 = xla_ops.einsum(x_i, y_i, "ab,bc->ac")
z5 = xla_ops.einsum(y_i, x_i, "cd,ce->de")  # Includes transpose.
outputs = [z1, z2, z3, z4, z5]
exit(outputs)
