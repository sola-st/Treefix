# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
broadcast_shape = array_ops.broadcast_dynamic_shape(
    array_ops.shape(x), self.batch_shape_tensor())
zeros = array_ops.zeros(broadcast_shape, dtype=self.dtype)
ones = array_ops.ones(broadcast_shape, dtype=self.dtype)
broadcasted_x = x * ones
result_if_not_big = array_ops.where_v2(
    x < self.low, zeros, (broadcasted_x - self.low) / self.range())
exit(array_ops.where_v2(x >= self.high, ones, result_if_not_big))
