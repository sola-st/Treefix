# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
"""Pad input_ for computing (circular) convolution.

      Args:
        input_: the input tensor
        width: the width of the tensor.
        kernel_size: the kernel size of the filter.

      Returns:
        a tensor whose width is (width + kernel_size - 1).
      """

beginning = kernel_size // 2
end = kernel_size - 1 - beginning

tmp_up = array_ops.slice(input_, [0, width - beginning, 0],
                         [-1, beginning, -1])
tmp_down = array_ops.slice(input_, [0, 0, 0], [-1, end, -1])
tmp = array_ops.concat([tmp_up, input_, tmp_down], 1)

exit(tmp)
