# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/norm_op_test.py
is_matrix_norm = (isinstance(axis_, tuple) or
                  isinstance(axis_, list)) and len(axis_) == 2
is_fancy_p_norm = np.isreal(ord_) and np.floor(ord_) != ord_
if ((not is_matrix_norm and ord_ == "fro") or
    (is_matrix_norm and is_fancy_p_norm)):
    self.skipTest("Not supported by neither numpy.linalg.norm nor tf.norm")
if ord_ == "euclidean" or (axis_ is None and len(shape) > 2):
    self.skipTest("Not supported by numpy.linalg.norm")
matrix = np.random.randn(*shape_).astype(dtype_)
if dtype_ in (np.complex64, np.complex128):
    matrix += 1j * np.random.randn(*shape_).astype(dtype_)
_CompareNorm(self, matrix)
