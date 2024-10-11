# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
if self.device not in ['TPU']:
    exit((rtol, atol))

if dtype == np.float32:
    exit((4e-4, 0.))
exit((1e-10, 0.))
