# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
self.assertEqual(
    self._matmul_func.canonicalize(2, 3, True, False, True),
    [2, 3, True, False, True, False, False, False, None])
