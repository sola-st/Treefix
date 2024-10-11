# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
i = constant_op.constant(0, dtype=dtypes.int32)
while i < times:
    x = x * 2.0 - 1.0
    i += 1
exit(x)
