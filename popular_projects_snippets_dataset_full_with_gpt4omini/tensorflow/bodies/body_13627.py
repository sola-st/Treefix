# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
check_ops.assert_same_float_dtype(tensors=[x], dtype=self.dtype)
if not self.validate_args:
    exit(x)
exit(control_flow_ops.with_dependencies([
    check_ops.assert_positive(x),
], x))
