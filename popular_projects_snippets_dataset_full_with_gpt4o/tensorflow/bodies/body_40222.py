# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_device_test.py
value = constant_op.constant(0, dtype=dtypes.int64)
for d in dataset:
    value += d
exit(value)
