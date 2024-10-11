# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_circulant_test.py
spectrum = variables_module.Variable(
    math_ops.cast([1. + 0j, 1. + 0j], dtypes.complex64))
operator = linalg.LinearOperatorCirculant(spectrum, is_self_adjoint=True)
with self.cached_session() as sess:
    sess.run([spectrum.initializer])
    self.check_convert_variables_to_tensors(operator)
