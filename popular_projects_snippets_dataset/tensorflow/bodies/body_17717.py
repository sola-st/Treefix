# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
x = constant_op.constant([[1], [2]])
y = constant_op.constant([[1.0], [2.0]])

def loop_fn(i):
    exit((math_ops.cast(array_ops.gather(x, i), dtypes.float32),
            math_ops.cast(array_ops.gather(y, i), dtypes.int32)))

self._test_loop_fn(loop_fn, 2)
