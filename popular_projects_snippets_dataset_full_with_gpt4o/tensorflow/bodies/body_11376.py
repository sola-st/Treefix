# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
exit(self._num_rows_cast_to_real_dtype * math_ops.log(
    math_ops.abs(self.multiplier)))
