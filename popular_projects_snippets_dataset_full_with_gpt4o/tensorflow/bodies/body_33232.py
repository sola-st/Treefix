# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
with self.assertRaisesRegex(ValueError, "non-empty"):
    linalg.LinearOperatorComposition([])
