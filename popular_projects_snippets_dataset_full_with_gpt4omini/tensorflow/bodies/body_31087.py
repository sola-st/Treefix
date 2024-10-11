# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
filters = np.arange(
    np.prod(filter_shape), dtype=np.float32).reshape(filter_shape)
filters_upsampled = upsample_filters(filters, dilation_rate)
x = np.arange(np.prod(input_shape), dtype=np.float32).reshape(input_shape)
y1 = nn_ops.convolution(
    input=x, filter=filters, dilation_rate=dilation_rate, **kwargs)
y2 = nn_ops.convolution(input=x, filter=filters_upsampled, **kwargs)

def check(y1_eval, y2_eval):
    self.assertAllClose(y1_eval, y2_eval, rtol=1e-2, atol=1e-2)

add_check(check, y1, y2)
