# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
super(FunctionParameterCanonicalizerTest, self).setUp()
self._matmul_func = (
    _function_parameter_canonicalizer_binding_for_test
    .FunctionParameterCanonicalizer([
        'a', 'b', 'transpose_a', 'transpose_b', 'adjoint_a', 'adjoint_b',
        'a_is_sparse', 'b_is_sparse', 'name'
    ], (False, False, False, False, False, False, None)))
