# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
with self.assertRaisesRegex(TypeError,
                            'Missing required positional argument'):
    self._matmul_func.canonicalize(
        transpose_a=True, transpose_b=True, adjoint_a=True)
