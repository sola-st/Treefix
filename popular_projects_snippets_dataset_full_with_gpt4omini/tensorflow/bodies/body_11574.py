# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
x_mat = array_ops.expand_dims(x, axis=-1)
y_mat = self.matmul(x_mat, adjoint=adjoint)
exit(array_ops.squeeze(y_mat, axis=-1))
