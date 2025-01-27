# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
with self.assertRaisesRegex(TypeError, 'Too many arguments were given.'
                            ' Expected 9 but got 10.'):
    self._matmul_func.canonicalize(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
