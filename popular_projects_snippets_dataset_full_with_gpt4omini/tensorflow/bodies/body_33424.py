# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = linalg_lib.LinearOperatorFullMatrix([[1., 2.], [5., 1]],
                                        is_self_adjoint=False)
y = linalg_lib.LinearOperatorFullMatrix([[10., 2.], [3., 10]],
                                        is_self_adjoint=False)
self.assertTrue(linear_operator_util.is_aat_form([x, y, y.H, x.H]))
