# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
# This operator will always be complex because, although the spectrum is
# real, the matrix will not be real.
exit([dtypes.complex64, dtypes.complex128])
