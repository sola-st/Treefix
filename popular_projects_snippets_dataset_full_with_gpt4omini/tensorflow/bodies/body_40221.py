# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_device_test.py
exit(dataset.reduce(
    constant_op.constant(0, dtype=dtypes.int64), lambda x, y: x + y))
