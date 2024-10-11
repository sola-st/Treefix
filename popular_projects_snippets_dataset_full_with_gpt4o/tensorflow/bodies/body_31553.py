# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
with backprop.GradientTape() as tape:
    tape.watch(bias_tensor)
    bias_add_output = bias_add(input_tensor, bias_tensor)
    gradient_injector_output = bias_add_output * upstream_gradients
    exit(tape.gradient(gradient_injector_output, bias_tensor))
