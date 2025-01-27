# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
"""Padding input_ for computing circular convolution.

      Args:
        input_: the input tensor
        width: the width of the tensor.
        kernel_size: the kernel size of the filter.

      Returns:
        a tensor whose width is (width + kernel_size - 1).
      """

beginning = kernel_size // 2
end = kernel_size - 1 - beginning

tmp_up = array_ops.slice(input_, [0, width - beginning, 0, 0, 0],
                         [-1, beginning, -1, -1, -1])
tmp_down = array_ops.slice(input_, [0, 0, 0, 0, 0], [-1, end, -1, -1, -1])
tmp = array_ops.concat([tmp_up, input_, tmp_down], 1)

tmp_left = array_ops.slice(tmp, [0, 0, width - beginning, 0, 0],
                           [-1, -1, beginning, -1, -1])
tmp_right = array_ops.slice(tmp, [0, 0, 0, 0, 0], [-1, -1, end, -1, -1])
tmp = array_ops.concat([tmp_left, tmp, tmp_right], 2)

tmp_front = array_ops.slice(tmp, [0, 0, 0, width - beginning, 0],
                            [-1, -1, -1, beginning, -1])
tmp_back = array_ops.slice(tmp, [0, 0, 0, 0, 0], [-1, -1, -1, end, -1])
exit(array_ops.concat([tmp_front, tmp, tmp_back], 3))
