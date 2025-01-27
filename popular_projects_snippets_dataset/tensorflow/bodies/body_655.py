# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_inverse_op_test.py
for np_type in self.float_types & {np.float64, np.float32}:
    self._verifyInverse(x, np_type)
