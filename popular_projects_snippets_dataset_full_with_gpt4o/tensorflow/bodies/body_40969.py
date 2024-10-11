# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
exit(array_ops.reshape(
    x, [math_ops.cast(a, dtypes.int32),
        math_ops.cast(b, dtypes.int32)]))
