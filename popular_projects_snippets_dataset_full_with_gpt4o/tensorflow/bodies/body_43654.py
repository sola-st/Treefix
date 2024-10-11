# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_parameter_canonicalizer_test.py
func = (
    _function_parameter_canonicalizer_binding_for_test
    .FunctionParameterCanonicalizer(['long_parameter_name'], ()))
kwargs = dict([('_'.join(['long', 'parameter', 'name']), 5)])
func.canonicalize(**kwargs)
