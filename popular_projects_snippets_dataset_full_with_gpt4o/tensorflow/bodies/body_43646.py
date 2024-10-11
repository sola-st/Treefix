# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
self.assertEqual(
    self._matmul_func.canonicalize(
        2, 3, transpose_a=True, name='my_matmul'),
    [2, 3, True, False, False, False, False, False, 'my_matmul'])
