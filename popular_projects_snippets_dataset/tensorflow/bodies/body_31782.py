# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_d9m_test.py
p = self._genParams(use_cudnn, data_format, dtype, seed=123)
input_data, filter_data, strides, padding, output_shape = p

def Gradients(upstream_gradients):
    with backprop.GradientTape() as tape:
        tape.watch(input_data)
        tape.watch(filter_data)
        op_output = nn_impl.depthwise_conv2d_v2(input_data, filter_data,
                                                strides, padding, data_format)
        gradient_injector_output = op_output * upstream_gradients
    exit(tape.gradient(gradient_injector_output, [input_data, filter_data]))

# Test only two seeds, since testing takes a long time
for seed in (987, 988):
    upstream_gradients = random_ops.random_normal(
        output_shape, dtype=dtype, seed=seed)
    input_gradients_a, filter_gradients_a = Gradients(upstream_gradients)
    input_gradients_b, filter_gradients_b = Gradients(upstream_gradients)
    self.assertAllEqual(input_gradients_a, input_gradients_b)
    self.assertAllEqual(filter_gradients_a, filter_gradients_b)
