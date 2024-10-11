# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
np.random.seed(local_seed)
upstream_gradients = self._randomDataOp(output_shape, data_type)
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(bias_val)
    bias_add_output = nn_ops.bias_add(
        input_val, bias_val, data_format=data_format)
    gradient_injector_output = bias_add_output * upstream_gradients
exit(tape.gradient(gradient_injector_output, bias_val))
