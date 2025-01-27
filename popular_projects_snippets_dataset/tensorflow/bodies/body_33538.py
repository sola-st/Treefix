# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py
matrix = [[0., 1.], [2., 3.]]
for ord_ in "fro", -7, -1.1, 0:
    with self.assertRaisesRegex(ValueError,
                                "'ord' must be a supported vector norm"):
        linalg_ops.norm(matrix, ord=ord_)

for ord_ in "fro", -7, -1.1, 0:
    with self.assertRaisesRegex(ValueError,
                                "'ord' must be a supported vector norm"):
        linalg_ops.norm(matrix, ord=ord_, axis=-1)

for ord_ in "foo", -7, -1.1, 1.1:
    with self.assertRaisesRegex(ValueError,
                                "'ord' must be a supported matrix norm"):
        linalg_ops.norm(matrix, ord=ord_, axis=[-2, -1])
