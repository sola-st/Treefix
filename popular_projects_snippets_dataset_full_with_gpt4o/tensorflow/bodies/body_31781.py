# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
with backprop.GradientTape() as tape:
    tape.watch(input_data)
    tape.watch(filter_data)
    op_output = nn_impl.depthwise_conv2d_v2(input_data, filter_data,
                                            strides, padding, data_format)
    gradient_injector_output = op_output * upstream_gradients
exit(tape.gradient(gradient_injector_output, [input_data, filter_data]))
