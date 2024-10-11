# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# If no GPU available, skip the test
if not test.is_gpu_available(cuda_only=True):
    exit()
large_shapes = [[4, 10, 10, 10, 3], [4, 10, 10, 10, 8], [4, 10, 10, 10, 13],
                [4, 3, 10, 10, 10], [4, 8, 10, 10, 10], [4, 13, 10, 10,
                                                         10]] * 3
perms = [[0, 4, 1, 2, 3]] * 3 + [[0, 2, 3, 4, 1]] * 3 + [[
    4, 1, 2, 3, 0
]] * 6 + [[1, 2, 3, 4, 0]] * 6

datatypes = [
    np.int8, np.float16, np.float32, np.float64, np.complex128,
    dtypes.bfloat16.as_numpy_dtype
]
for datatype in datatypes:
    for input_shape, perm in zip(large_shapes, perms):
        with self.subTest(
            datatype=datatype, input_shape=input_shape, perm=perm):
            total_size = np.prod(input_shape)
            inp = np.arange(
                1, total_size + 1, dtype=datatype).reshape(input_shape)
            np_ans = self._np_transpose(inp, perm)
            with self.cached_session():
                inx = ops.convert_to_tensor(inp)
                y = array_ops.transpose(inx, perm)
                tf_ans = self.evaluate(y)
            self.assertAllEqual(np_ans, tf_ans)
            self.assertShapeEqual(np_ans, y)
