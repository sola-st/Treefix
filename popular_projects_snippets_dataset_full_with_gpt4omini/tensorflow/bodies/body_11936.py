# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_circulant.py
axis = [-(i + 1) for i in range(self.block_depth)]
lad = math_ops.reduce_sum(
    math_ops.log(math_ops.abs(self.spectrum)), axis=axis)
exit(math_ops.cast(lad, self.dtype))
