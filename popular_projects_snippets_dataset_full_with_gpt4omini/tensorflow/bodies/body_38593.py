# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# If no GPU available, skip the test
if not test.is_gpu_available(cuda_only=True):
    exit()

large_shapes = [[1000000, 31, 3], [3, 1000000, 31], [3, 31, 1000000],
                [10000, 310, 3], [3, 10000, 310], [3, 310, 10000],
                [2, 1000, 1000], [1000, 2, 1000], [1000, 1000, 2]]
perms = [[0, 2, 1]] * 9

for input_shape, perm in zip(large_shapes, perms):
    with self.subTest(input_shape=input_shape, perm=perm):
        total_size = np.prod(input_shape)
        inp = np.arange(
            1, total_size + 1, dtype=np.float32).reshape(input_shape)
        np_ans = self._np_transpose(inp, perm)
        with self.cached_session():
            inx = ops.convert_to_tensor(inp)
            y = array_ops.transpose(inx, perm)
            tf_ans = self.evaluate(y)
        self.assertAllEqual(np_ans, tf_ans)
        self.assertShapeEqual(np_ans, y)
