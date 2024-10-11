# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
binary_output = True
inp = random_ops.random_uniform(
    shape=[10, 10],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.int32,
    seed=-2460)
size = random_ops.random_uniform(
    shape=[], minval=-10000, maxval=10000, dtype=dtypes.int32, seed=-10000)
weights = random_ops.random_uniform(
    shape=[],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.float32,
    seed=-10000)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(
        gen_math_ops.dense_bincount(
            input=inp,
            size=size,
            weights=weights,
            binary_output=binary_output))
