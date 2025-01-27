# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
with self.session():
    with self.assertRaises((errors.InvalidArgumentError, ValueError)):
        op = array_ops.matrix_diag(
            k=1070828000000, diagonal=np.ones((2, 2, 2, 2)))
        self.evaluate(op)
