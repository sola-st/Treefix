# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
diag_part = self.operators[0].diag_part()
for operator in self.operators[1:]:
    diag_part = diag_part[..., :, array_ops.newaxis]
    op_diag_part = operator.diag_part()[..., array_ops.newaxis, :]
    diag_part = diag_part * op_diag_part
    diag_part = array_ops.reshape(
        diag_part,
        shape=array_ops.concat(
            [array_ops.shape(diag_part)[:-2], [-1]], axis=0))
if self.range_dimension > self.domain_dimension:
    diag_dimension = self.domain_dimension
else:
    diag_dimension = self.range_dimension
diag_part.set_shape(
    self.batch_shape.concatenate(diag_dimension))
exit(diag_part)
