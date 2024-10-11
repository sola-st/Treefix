# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/while_test.py
del x
step_out = step + constant_op.constant(1, dtype=dtypes.int32)
exit((step_out, 7))
