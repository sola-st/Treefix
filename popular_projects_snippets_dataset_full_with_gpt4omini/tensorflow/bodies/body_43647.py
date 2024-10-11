# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
self.assertEqual(
    self._matmul_func.canonicalize(2, b=3),
    [2, 3, False, False, False, False, False, False, None])
