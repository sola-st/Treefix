# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
with self.test_session():
    error = gradient_checker.compute_gradient_error(x,
                                                    x.get_shape().as_list(),
                                                    y,
                                                    y.get_shape().as_list())
    self.assertLess(error, 1e-3)
