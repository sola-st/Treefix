# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
self.setUp()
with self.session(use_gpu=use_gpu):
    var_t = variables.VariableV1(var)
    m_t = variables.VariableV1(m)
    v_t = variables.VariableV1(v)

    t = 1
    beta1 = np.array(0.9, dtype=var.dtype)
    beta2 = np.array(0.999, dtype=var.dtype)
    beta1_power = beta1**t
    beta2_power = beta2**t
    lr = np.array(0.001, dtype=var.dtype)
    epsilon = np.array(1e-8, dtype=var.dtype)
    beta1_t = constant_op.constant(beta1, self._toType(var.dtype), [])
    beta2_t = constant_op.constant(beta2, self._toType(var.dtype), [])
    beta1_power_t = variables.VariableV1(beta1_power)
    beta2_power_t = variables.VariableV1(beta2_power)
    lr_t = constant_op.constant(lr, self._toType(var.dtype), [])
    epsilon_t = constant_op.constant(epsilon, self._toType(var.dtype), [])
    self.evaluate(variables.global_variables_initializer())

    self.assertAllCloseAccordingToType(var, self.evaluate(var_t))
    new_var, _, _ = self._adamUpdateNumpy(var, grad, t, m, v, lr, beta1,
                                          beta2, epsilon)
    apply_adam = training_ops.apply_adam(var_t, m_t, v_t, beta1_power_t,
                                         beta2_power_t, lr_t, beta1_t,
                                         beta2_t, epsilon_t, grad)
    out = self.evaluate(apply_adam)
    self.assertShapeEqual(out, apply_adam)
    self.assertAllCloseAccordingToType(new_var, out)
