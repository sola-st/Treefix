# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
if use_gpu and not test.is_gpu_available(cuda_only=True):
    exit()
if not use_gpu and dilations != (1, 1):
    exit()  # Non-default dilations is currently not supported on the CPU.

x1 = self._CreateNumpyTensor(filter_sizes)
x2 = self._CreateNumpyTensor(output_sizes)
dilations = list(dilations)
padded_input_sizes = input_sizes[:]
padded_input_sizes[1] += padding[0][0] + padding[0][1]
padded_input_sizes[2] += padding[1][0] + padding[1][1]
c = nn_ops.conv2d_backprop_input(
    padded_input_sizes,
    x1,
    x2,
    strides=[1] + strides + [1],
    padding="VALID",
    dilations=[1] + dilations + [1])
c = c[:, padding[0][0]:(c.shape[1] - padding[0][1]), padding[1][0]:(
    c.shape[2] - padding[1][1]), :]
expected = list(self.evaluate(array_ops.reshape(c, [-1])))
self._RunAndVerifyBackpropInput(
    input_sizes,
    filter_sizes,
    output_sizes,
    strides,
    padding,
    expected,
    data_format,
    use_gpu=use_gpu,
    err=err,
    dilations=dilations)
