# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
x = array_ops.placeholder(dtypes.int32)
values = np.zeros([5, 30])
splits = array_ops.placeholder(dtypes.int32)
with self.assertRaisesRegex(ValueError, "Cannot infer"):
    y = array_ops.split(values, splits, axis=x)

splits = array_ops.placeholder(dtypes.int32, [3])
y = array_ops.split(values, splits, axis=x)
with self.session() as sess:
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "must have exactly one element"):
        sess.run(y, {x: np.array([], dtype=np.int32), splits: [4, 11, 15]})
