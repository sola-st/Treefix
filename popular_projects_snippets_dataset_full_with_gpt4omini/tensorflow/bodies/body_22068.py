# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent_test.py
for dtype in [dtypes.half, dtypes.float32, dtypes.float64]:
    # train.GradientDescentOptimizer is V1 only API.
    with ops.Graph().as_default(), self.cached_session():
        opt = gradient_descent.GradientDescentOptimizer(3.0)
        values = [1.0, 3.0]
        vars_ = [variables.Variable([v], dtype=dtype) for v in values]
        grads_and_vars = opt.compute_gradients(vars_[0] + vars_[1], vars_)
        self.evaluate(variables.global_variables_initializer())
        for grad, _ in grads_and_vars:
            self.assertAllCloseAccordingToType([1.0], self.evaluate(grad))
