# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/logging_ops_test.py
ind = [[0, 0], [1, 0], [1, 3], [4, 1], [1, 4], [3, 2], [3, 3]]
val = [0, 10, 13, 4, 14, 32, 33]
shape = [5, 6]

sparse = sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.int64),
    constant_op.constant(shape, dtypes.int64))

with self.captureWritesToStream(sys.stderr) as printed:
    print_op = logging_ops.print_v2(sparse)
    self.evaluate(print_op)
expected = ("'SparseTensor(indices=[[0 0]\n"
            " [1 0]\n"
            " [1 3]\n"
            " ...\n"
            " [1 4]\n"
            " [3 2]\n"
            " [3 3]], values=[0 10 13 ... 14 32 33], shape=[5 6])'")
self.assertIn((expected + "\n"), printed.contents())
