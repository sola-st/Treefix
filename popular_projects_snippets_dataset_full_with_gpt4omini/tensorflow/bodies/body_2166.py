# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
step_out = step + constant_op.constant(1, dtype=dtypes.int32)
sum_out = rsum + constant_op.constant(1.5, dtype=dtypes.float32)
exit((step_out, sum_out))
