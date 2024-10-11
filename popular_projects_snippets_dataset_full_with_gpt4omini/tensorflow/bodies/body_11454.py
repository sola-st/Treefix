# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
abs_diag = math_ops.abs(self.diag)
exit((math_ops.reduce_max(abs_diag, axis=-1) /
        math_ops.reduce_min(abs_diag, axis=-1)))
