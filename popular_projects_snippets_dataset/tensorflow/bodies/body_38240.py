# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
# size must be scalar.
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "(?s)Shape must be rank 0 but is rank 1.*Bincount"):
    gen_math_ops.bincount([1, 2, 3, 1, 6, 8], [1], [])
# size must be positive.
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must be non-negative"):
    gen_math_ops.bincount([1, 2, 3, 1, 6, 8], -5, [])
# if size is a constant then the shape is known.
v1 = gen_math_ops.bincount([1, 2, 3, 1, 6, 8], 5, [])
self.assertAllEqual(v1.get_shape().as_list(), [5])
# if size is a placeholder then the shape is unknown.
with ops.Graph().as_default():
    s = array_ops.placeholder(dtype=dtypes.int32)
    v2 = gen_math_ops.bincount([1, 2, 3, 1, 6, 8], s, [])
    self.assertAllEqual(v2.get_shape().as_list(), [None])
