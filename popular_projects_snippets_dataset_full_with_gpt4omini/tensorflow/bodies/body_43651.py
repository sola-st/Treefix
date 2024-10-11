# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
with self.assertRaisesRegex(TypeError,
                            'Got an unexpected keyword argument'):
    self._matmul_func.canonicalize(2, 3, hohoho=True)
