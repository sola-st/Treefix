# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# pyformat: disable
paddings_values = [[[0, 0], [0, 0], [0, 0], [0, 1]],
                   [[0, 0], [2, 3], [0, 0], [0, 0]],
                   [[0, 0], [0, 0], [0, 0], [0, 0]]]
# pyformat: enable
for paddings_value in paddings_values:
    for dtype in [dtypes.float32, dtypes.int32]:
        inp = constant_op.constant(1, shape=[8, 28, 28, 3], dtype=dtype)
        paddings = constant_op.constant(paddings_value, dtype=dtypes.int32)
        padded = array_ops.pad(inp, paddings)
        middle = array_ops.slice(padded, [row[0] for row in paddings_value],
                                 [dim.value for dim in inp.shape.dims])
        left = array_ops.slice(padded, [0, 0, 0, 0],
                               [row[0] for row in paddings_value])
        right = array_ops.slice(
            padded,
            [paddings_value[i][0] + inp.shape.dims[i].value for i in range(4)],
            [-1, -1, -1, -1])
        with self.cached_session():
            self.assertAllEqual(inp, self.evaluate(middle))
            self.assertAllEqual(
                np.zeros([row[0] for row in paddings_value]), self.evaluate(left))
            self.assertAllEqual(
                np.zeros([row[1] for row in paddings_value]),
                self.evaluate(right))
