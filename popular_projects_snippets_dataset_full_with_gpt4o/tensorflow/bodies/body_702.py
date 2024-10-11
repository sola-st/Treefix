# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/special_math_test.py
if self.device not in ['XLA_GPU', 'XLA_CPU'] and dtype == np.float64:
    self.skipTest(
        'Skipping test because some F64 operations not supported on TPU.')
