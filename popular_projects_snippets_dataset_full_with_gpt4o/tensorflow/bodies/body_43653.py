# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
with self.assertRaisesRegex(
    TypeError, "Got multiple values for argument 'transpose_a'"):
    self._matmul_func.canonicalize(2, 3, False, transpose_a=True)
