# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
broadcasted_x = x * array_ops.ones(
    self.batch_shape_tensor(), dtype=x.dtype)
exit(array_ops.where_v2(
    math_ops.is_nan(broadcasted_x), broadcasted_x,
    array_ops.where_v2(
        math_ops.logical_or(broadcasted_x < self.low,
                            broadcasted_x >= self.high),
        array_ops.zeros_like(broadcasted_x),
        array_ops.ones_like(broadcasted_x) / self.range())))
