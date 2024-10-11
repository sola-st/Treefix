# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
exit(set(self.numeric_types) - set(
    self.complex_types) - {np.uint64, np.int64, np.uint8, np.int8})
