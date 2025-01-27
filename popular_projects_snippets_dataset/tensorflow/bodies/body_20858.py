# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=use_gpu):
    var = variables.VariableV1(x)
    accum = variables.VariableV1(y)
    linear = variables.VariableV1(z)
    self.evaluate(variables.global_variables_initializer())

    self.assertAllCloseAccordingToType(x, self.evaluate(var))
    apply_ftrl = training_ops.apply_ftrl(var, accum, linear, grad, lr, l1, l2,
                                         lr_power)
    out = self.evaluate(apply_ftrl)
    self.assertShapeEqual(out, apply_ftrl)
    accum_update = y + grad * grad
    linear_update = z + grad - (accum_update**(-lr_power) - y**
                                (-lr_power)) / lr * x
    quadratic = 1.0 / (accum_update**(lr_power) * lr) + 2 * l2
    expected_out = np.array([(
        np.sign(linear_update[i]) * l1 - linear_update[i]) / (quadratic[i]) if
                             np.abs(linear_update[i]) > l1 else 0.0
                             for i in range(linear_update.size)])
    self.assertAllCloseAccordingToType(accum_update, self.evaluate(accum))
    if x.dtype == np.float16:
        # The calculations here really are not very precise in float16.
        self.assertAllClose(
            linear_update, self.evaluate(linear), rtol=2e-2, atol=2e-2)
        self.assertAllClose(expected_out, out, rtol=2e-2, atol=2e-2)
    elif x.dtype == np.float32:
        # The calculations here not sufficiently precise in float32.
        self.assertAllClose(
            linear_update, self.evaluate(linear), rtol=1e-5, atol=1e-5)
        self.assertAllClose(expected_out, out, rtol=1e-5, atol=1e-5)
    else:
        self.assertAllClose(linear_update, self.evaluate(linear))
        self.assertAllClose(expected_out, out)
