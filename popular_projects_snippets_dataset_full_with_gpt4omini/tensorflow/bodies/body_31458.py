# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if use_gpu and not test.is_gpu_available(cuda_only=True):
    exit()
if not use_gpu and dilations != (1, 1):
    exit()  # Non-default dilations is currently not supported on the CPU.

x0 = self._CreateNumpyTensor(input_sizes)
x2 = self._CreateNumpyTensor(output_sizes)
dilations = list(dilations)

x0 = np.pad(x0, [(0, 0)] + padding + [(0, 0)], "constant")
c = nn_ops.conv2d_backprop_filter(
    x0,
    filter_sizes,
    x2,
    strides=[1] + strides + [1],
    padding="VALID",
    dilations=[1] + dilations + [1])
expected = list(self.evaluate(array_ops.reshape(c, [-1])))
self._RunAndVerifyBackpropFilter(
    input_sizes,
    filter_sizes,
    output_sizes,
    strides,
    padding,
    expected,
    data_format,
    use_gpu=use_gpu,
    dilations=dilations,
    err=err)
