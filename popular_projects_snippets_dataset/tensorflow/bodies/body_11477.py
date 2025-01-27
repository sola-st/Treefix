# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
# Slice the batch shape and return a new LinearOperatorIdentity.
# Use a proxy shape and slice it. Use this as the new batch shape
new_batch_shape = array_ops.shape(
    array_ops.ones(self._batch_shape_arg)[slices])
parameters = dict(self.parameters, batch_shape=new_batch_shape)
exit(LinearOperatorZeros(**parameters))
