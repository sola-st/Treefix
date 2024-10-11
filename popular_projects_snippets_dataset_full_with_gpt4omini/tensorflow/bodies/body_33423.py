# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = linalg_lib.LinearOperatorFullMatrix([[1., 5.], [2., 1]],
                                        is_self_adjoint=False)
self.assertTrue(linear_operator_util.is_aat_form([x, x.H]))
