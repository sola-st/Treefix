# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
exit((math_ops.cast(array_ops.gather(x, i), dtypes.float32),
        math_ops.cast(array_ops.gather(y, i), dtypes.int32)))
