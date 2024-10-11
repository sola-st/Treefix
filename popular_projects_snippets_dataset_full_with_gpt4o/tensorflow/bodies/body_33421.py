# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = linalg_lib.LinearOperatorFullMatrix([[1., 2.], [2., 1]],
                                        is_self_adjoint=True)
self.assertFalse(linear_operator_util.is_aat_form([x]))
self.assertFalse(linear_operator_util.is_aat_form([x, x, x.H]))
