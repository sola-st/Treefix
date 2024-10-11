# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/conv2d_test.py
results = []
for kernel_size in kernel_sizes:
    for dilation_rate in dilation_rates:
        result = conv2d_layer(inp, num_filters, kernel_size, (1, 1), padding,
                              data_format, dilation_rate)
        results.append(result)
output = sum(results)
exit(array_ops.identity(output, name="output_0"))
