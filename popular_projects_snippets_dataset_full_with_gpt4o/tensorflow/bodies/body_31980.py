# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
total_input_size = 1
total_filter_size = 1
for s in input_sizes:
    total_input_size *= s
for s in filter_sizes:
    total_filter_size *= s
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x1 = [f * 1.0 for f in range(1, total_input_size + 1)]
x2 = [f * 1.0 for f in range(1, total_filter_size + 1)]
default_dilations = (
    dilations[0] == 1 and dilations[1] == 1 and dilations[2] == 1)

# If any dilation rate is larger than 1, only do test on the GPU
# because we currently do not have a CPU implementation for arbitrary
# dilation rates.
if default_dilations or use_gpu:
    with self.cached_session(use_gpu=use_gpu) as sess:
        if data_format == "NCDHW":
            input_sizes = test_util.NHWCToNCHW(input_sizes)
        t1 = constant_op.constant(x1, shape=input_sizes)
        t2 = constant_op.constant(x2, shape=filter_sizes)
        full_strides = [1] + strides + [1]
        full_dilations = [1] + dilations + [1]
        if data_format == "NCDHW":
            full_strides = test_util.NHWCToNCHW(full_strides)
            full_dilations = test_util.NHWCToNCHW(full_dilations)
        actual = nn_ops.conv3d(
            t1,
            t2,
            strides=full_strides,
            dilations=full_dilations,
            padding=padding,
            data_format=data_format)
        expected = nn_ops.convolution(
            t1,
            t2,
            padding=padding,
            strides=strides,
            dilation_rate=dilations,
            data_format=data_format)
        if data_format == "NCDHW":
            actual = test_util.NCHWToNHWC(actual)
            expected = test_util.NCHWToNHWC(expected)
        actual_grad = gradients_impl.gradients(actual, t1
                                               if mode == "input" else t2)[0]
        expected_grad = gradients_impl.gradients(expected, t1
                                                 if mode == "input" else t2)[0]
        # "values" consists of two tensors for two backprops
        actual_value = self.evaluate(actual_grad)
        expected_value = self.evaluate(expected_grad)
        self.assertShapeEqual(actual_value, actual_grad)
        self.assertShapeEqual(expected_value, expected_grad)
    print("expected = ", expected_value)
    print("actual = ", actual_value)
    self.assertArrayNear(expected_value.flatten(), actual_value.flatten(),
                         err)
