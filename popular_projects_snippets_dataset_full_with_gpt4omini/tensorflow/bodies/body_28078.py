# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/rejection_resample_test.py
exit(math_ops.cast(
    random_ops.random_uniform([1]) * num_classes, dtypes.int32)[0])
