# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/transpose_op_test.py
# If no GPU available, skip the test
if not test.is_gpu_available(cuda_only=True):
    exit()
large_shapes = [[4, 10, 10, 3], [4, 10, 10, 8], [4, 10, 10, 13],
                [4, 3, 10, 10], [4, 8, 10, 10], [4, 13, 10, 10]] * 3
perms = [[0, 3, 1, 2]] * 3 + [[0, 2, 3, 1]] * 3 + [[3, 1, 2, 0]] * 6 + [[
    1, 2, 3, 0
]] * 3 + [[2, 3, 0, 1]] * 3

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

    # shapes related to Inception (taken from conv_ops_test.py)
inception_shapes = [[4, 5, 5, 124], [4, 8, 8, 38], [4, 8, 8, 38], [
    4, 8, 8, 204
], [4, 8, 8, 44], [4, 8, 8, 204], [4, 8, 8, 204], [4, 8, 8, 204], [
    4, 8, 8, 176
], [4, 8, 8, 176], [4, 8, 8, 176], [4, 8, 8, 176], [4, 17, 17, 19], [
    4, 17, 17, 19
], [4, 17, 17, 124], [4, 17, 17, 12], [4, 17, 17, 124], [4, 17, 17, 22], [
    4, 17, 17, 19
], [4, 17, 17, 19], [4, 17, 17, 121], [4, 17, 17, 121], [4, 17, 17, 22], [
    4, 17, 17, 19
], [4, 17, 17, 19], [4, 17, 17, 115], [4, 17, 17, 115], [4, 17, 17, 19], [
    4, 17, 17, 16
], [4, 17, 17, 115], [4, 17, 17, 102], [4, 17, 17, 12], [4, 17, 17, 102], [
    4, 17, 17, 12
], [4, 17, 17, 102], [4, 17, 17, 12], [4, 17, 17, 76], [4, 17, 17, 12], [
    4, 17, 17, 12
], [4, 17, 17, 76], [4, 17, 17, 76], [4, 35, 35, 9], [4, 35, 35, 28], [
    4, 35, 35, 6
], [4, 35, 35, 28], [4, 35, 35, 25], [4, 35, 35, 4], [4, 35, 35, 25],
                    [4, 35, 35, 9], [4, 35, 35, 19], [4, 35, 35, 19],
                    [4, 35, 35, 19], [4, 73, 73, 6], [4, 73, 73,
                                                      6], [4, 147, 147, 2]]
for input_shape in inception_shapes:
    with self.subTest(input_shape=input_shape):
        perm = [0, 3, 1, 2]
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
