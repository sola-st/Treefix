# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
if self.kernel is None:
    self.kernel = variables.Variable(
        array_ops.ones(
            array_ops.stack([self.output_size,
                             array_ops.shape(x)[-1]])))
    self.bias = variables.Variable(array_ops.ones([self.output_size]))
exit(math_ops.matmul(x, self.kernel, transpose_b=True) + self.bias)
