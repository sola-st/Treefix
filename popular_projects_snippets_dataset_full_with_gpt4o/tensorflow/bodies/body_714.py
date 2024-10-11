# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
if self.device not in ['TPU']:
    exit((rtol, atol))

if dtype == np.float32:
    exit((2e-2, 1e-7))
exit((2e-4, 1e-20))
