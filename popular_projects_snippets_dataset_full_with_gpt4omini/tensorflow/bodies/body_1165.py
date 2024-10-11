# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cholesky_op_test.py
exit(set(super(CholeskyOpTest, self).float_types).intersection(
    (np.float64, np.float32, np.complex64, np.complex128)))
